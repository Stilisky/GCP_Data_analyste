val <- seq(1,3, by=0.5) # Creation d'un vecteur par bond de 0,5 entre 1 et 3
val
vect <- seq(1,3, length=10) # creation d'un vecteur ayant 10 éléments

rep(1, 3) # repete une valeur un nombre de fois
rep(c(1,3), each=3)
cot <- rep("cot", 100)
cal <- rep("cal", 50)
a <- c(cot, cal)
paste()
# La sélection
z <- 1:20

# Creation de matrice
abou <- c(23, 232, "H",2)
allen <- c("ef" ,4, 23,"bc")
jo <- c(1, 2, 3, 4)
math <- c(5.2, 6.3, NA, 6)
t1 <- matrix(c(abou, allen, jo, math), ncol = 4)
t1 <- data.frame(t1)
t1
nameCol <- c("Abou", "Allen", "Jo", "Mathe")
colnames(t1) <-  nameCol
t1
