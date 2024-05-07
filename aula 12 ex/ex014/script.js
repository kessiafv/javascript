function carregar () {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        //bom dia
        img.src = `morning.png`
        document.body.style.background = `#bc6f0b`
    } else if (hora >= 12 && hora < 18) {
        //boa tarde
        img.src = `afternoon.png`
        document.body.style.background = `#fc8d0f`
    } else {
        //boa noite
        img.src = `night.png`
        document.body.style.background = `#1b201e`
    }
}

