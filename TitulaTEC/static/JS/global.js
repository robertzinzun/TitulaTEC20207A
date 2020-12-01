function eliminarEdificio(id,nombre){
    if(confirm('¿Estas seguro de eliminar al Edificio:'+nombre+'?'))
        location.href='/edificios/delete/'+id;
}
function regresar(url){
    location.href="/"+url;
}