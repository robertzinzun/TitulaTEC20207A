var op="";
function mostrarDiv(id){
    document.getElementById(id).style.display="block";
}
function ocultarDiv(id){
    document.getElementById(id).style.display="none";
}
function inicializarDivs(){
    mostrarDiv("listadoGeneral");
    ocultarDiv("datosInviduales")
    consultaGeneral();
}
function nuevo(){
    op="c";
    document.getElementById("titulo").innerHTML="<h1> Registro de Edificios</h1>";
    ocultarDiv("listadoGeneral");
    reset();
    mostrarDiv("datosInviduales")
}
function editar(id){
    op="u";
    document.getElementById("titulo").innerHTML="<h1> Edicion de Edificios</h1>";
    ocultarDiv("listadoGeneral");
    reset();
    var obj=new Edificio(id,"");
    var obj2=obj.consultar();
    document.getElementById("id").value=obj2.id;
    document.getElementById("nombre").value=obj2.nombre;
    mostrarDiv("datosInviduales")
}
function realizarOperacion(){
    var obj;
    switch(op){
        case "c":
            obj=new Edificio(
                document.getElementById("id").value,
                document.getElementById("nombre").value);
            obj.guardar();    
            inicializarDivs();
            break;
        case "u":
            obj=new Edificio(
                document.getElementById("id").value,
                document.getElementById("nombre").value);
            obj.actualizar();    
            inicializarDivs();
            break;    
    }
}
function consultaGeneral(){
    var table=document.getElementById("datos");
    eliminarTabla();
    for(i=0;i<arrayEdificios.length;i++){
        var tr=document.createElement("tr");
        var objeto=arrayEdificios[i];
        for(p in objeto){
           var td=document.createElement("td");
           var txt=document.createTextNode(objeto[p]);
           td.appendChild(txt); 
           tr.appendChild(td);

        }
        var link=crearLink(arrayEdificios[i].id,"editar");
        var td=document.createElement("td");
        td.appendChild(link);
        tr.appendChild(td)
        link=crearLink(arrayEdificios[i].id,"eliminar");
        td=document.createElement("td");
        td.appendChild(link);
        tr.appendChild(td)
        table.appendChild(tr);
    }
}
function crearLink(id,operacion){
    var link=document.createElement("a");
    var img=document.createElement("img");
    img.setAttribute("src","../Imagenes/"+operacion+".png");
    link.appendChild(img);
    link.setAttribute("href","javascript:"+operacion+"("+id+")");
    return link;
}
function cancelar(){
    inicializarDivs();
}
function eliminarTabla(){
    var table=document.getElementById("datos");
    for(i=table.rows.length-1;i>0;i--){
        table.removeChild(table.rows[i])
    }
}
function reset(){
    document.getElementById("id").value="";
    document.getElementById("nombre").value="";
}