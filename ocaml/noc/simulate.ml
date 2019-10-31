open Owl
open Owl_ode
open Owl_ode.Types

let impulse ?c ~tau ~n ~a ~input duration =
  let tspec = T1 { t0 = 0.0; dt = 1E-3; duration } in
  let f =
    let z = Mat.(transpose a /$ tau) in
    fun x t ->
      let dx = Mat.(x *@ z) in
      if t < 0.05 || t > 0.055 then dx else Mat.(dx + (input /$ tau))
  in
  let ts, xs = Ode.odeint (module Owl_ode.Native.D.RK4) f Mat.(zeros 1 n) tspec () in
  let xs =
    match c with
    | Some c -> Mat.(xs *@ transpose c)
    | None   -> xs
  in
  Mat.concat_horizontal ts xs


let ou_process ~n ~dt ~tau duration =
  let t_max = 1 + int_of_float (duration /. dt) in
  let rec iter t x accu =
    if t = t_max
    then accu |> List.rev |> Array.of_list |> Mat.concatenate ~axis:0
    else (
      let accu = x :: accu in
      let x =
        Mat.((1. -. (dt /. tau) $* x) + (Maths.(sqrt (2. *. dt /. tau)) $* gaussian 1 n))
      in
      iter (succ t) x accu)
  in
  let table = iter 0 Mat.(gaussian 1 n) [] in
  table, fun t -> Mat.row table (int_of_float (t /. dt))
