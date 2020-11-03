function validar(form){
    var cad=validarNombre(form.nombre.value);
    cad+=validarTelefono(form.telefono.value);
    cad+=validarEmail(form.email.value);
    cad+=validarPasssword(form.password.value,form.pwdrepite.value);
    cad+=validarNC(form.nocontrol.value);
    cad+=validarCreditos(parseInt(form.creditos.value));
    cad+=validarCarrera(parseInt(form.carrera.options[form.carrera.options.selectedIndex].value));
    cad+=validarAnio(form.anioegreso.value);
    if(cad!=''){
        document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{
       return true; 
    }
}
function validarNombre(cad){
    if(cad.length==0){
        return 'Debes informar el nombre de la persona.<br>';
    }
    else{
        return '';
    }
}
function validarTelefono(cad){
    var ban=false;
    if(cad.length==12){    
       var patron=/\d{3}-\d{3}-\d{4}/;
       if(patron.test(cad)){
           return '';
       } 
       else{
            return 'El número de telefono no cumple el patrón ###-###-####.<br>';
       }
    }
    else{
        return 'El telefono debe ser de 12 caracteres. <br>'
    }
}
function validarEmail(cad){
    var patron=/[a-z]\w*@\w+.\w+.*/;
    if(patron.test(cad)){
        return '';
    }
    else{
        return "La cuenta de correo electrónico no tiene el formato correcto. <br>";
    }
}
function validarPasssword(pwd1,pwd2){
    if(pwd1!=pwd2){
        return "Las contraseñas no coinciden. <br>";
    }
    else{
        return '';
    }
}
function validarNC(cad){
    var patron=/\d{8}/;
    if(patron.test(cad)){
        return '';
    }
    else{
        return "El número de control debe ser de 8 dígitos <br>";
    }
}
function validarCreditos(valor){
    if(valor>=1 && valor<=260){
        return '';
    }
    else{
        return "Los creditos exceden el rango <br>"
    }
}
function validarCarrera(valor){
    if(valor==0){
        return 'Debes elegir una carrera<br>';
    }
    return '';
}
function validarAnio(anioEgreso){
    var fecha=new Date();
    var anioActual=fecha.getFullYear();
    if(anioEgreso>anioActual){
        return 'El año de egreso no debe ser mayor a:'+anioActual+"<br>";
    }
    return '';
}