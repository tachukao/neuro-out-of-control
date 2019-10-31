open Owl

let obsv ?c a =
  assert (Mat.(row_num a) = Mat.(col_num a));
  let c =
    match c with
    | Some c -> c
    | None   -> Mat.(eye (row_num a))
  in
  Linalg.D.lyapunov Mat.(transpose a) Mat.(neg (transpose c) *@ c)


let ctrl ?b a =
  assert (Mat.(row_num a) = Mat.(col_num a));
  let b =
    match b with
    | Some b -> b
    | None   -> Mat.(eye (row_num a))
  in
  Linalg.D.lyapunov a Mat.(neg b *@ transpose b)


let discrete_ctrl ?b a =
  assert (Mat.(row_num a) = Mat.(col_num a));
  let n = Mat.row_num a in
  let b =
    match b with
    | Some b -> b
    | None   -> Mat.(eye n)
  in
  Linalg.D.discrete_lyapunov a Mat.(b *@ transpose b)


let discrete_obsv ?c a =
  assert (Mat.(row_num a) = Mat.(col_num a));
  let n = Mat.row_num a in
  let c =
    match c with
    | Some c -> c
    | None   -> Mat.(eye n)
  in
  Linalg.D.discrete_lyapunov Mat.(transpose a) Mat.(transpose c *@ c)
