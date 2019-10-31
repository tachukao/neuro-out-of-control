open Owl

val impulse : ?c:Mat.mat -> tau:float -> n:int -> a:Mat.mat -> input:Mat.mat -> float -> Mat.mat
val ou_process : n:int -> dt:float -> tau:float -> float -> Mat.mat * (float -> Mat.mat)
