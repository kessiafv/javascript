let num = [5, 8, 2, 9, 3]
num [5] = 6
console.log(`Colocando em ordem crescente ${num.sort()}`)
console.log(`O comprimento do array é ${num.length}`)
console.log(`Nosso vetor é o ${num}`)

let pos = num.indexOf(1)
if (pos == -1) {
    console.log('O valor não foi encontrado')
} else
    console.log(`O valor 8 está na posição ${pos}`)