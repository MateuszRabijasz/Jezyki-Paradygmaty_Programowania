open System

printf "Podaj wagę (kg): "
let weight = Console.ReadLine() |> float
printf "Podaj wzrost (cm): "
let height = Console.ReadLine() |> float

let dzielnik = 100.0
let waga = height / dzielnik
let bmi = weight / (waga * waga)

let category =
    if bmi < 18.5 then "Niedowaga"
    elif bmi < 24.9 then "Prawidłowa waga"
    elif bmi < 29.9 then "Nadwaga"
    else "Otyłość"

printfn "Twoje BMI: %.2f" bmi
printfn "Kategoria BMI: %s" category
