window.addEventListener('load', () => {
    let elements = document.querySelectorAll("#blog_title");
    elements.forEach(el => {
        console.log(el.textContent.trim());
        let b = el.textContent.trim()
        console.log("uzunligi ",b.length);
        if (b.length<44) {
            console.log(b);
        }else{
            b =  b.slice(0, 44)
            b+='...'
        }
        console.log("oxgardi :", b);
        
        el.innerHTML = b
        
        
    });
});
