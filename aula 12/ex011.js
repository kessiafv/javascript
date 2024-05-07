var idade = 66
console.log(`Você tem ${idade} anos.`)
if (idade < 16) {
    console.log(`E você não é obrigado a votar!`)
} else if (idade < 18 || idade > 65) {
    console.log(`O voto é opcional!`)
} else {
    console.log(`Voto obrigatório!`)
}