var operacion='';
function mostrarDiv(div,bandera){
    if(bandera==true){
        document.getElementById(div).style.display='block';
    }
    else{
        document.getElementById(div).style.display='none';
    }
}
function inicializarDivs(){
    operacion='';
    mostrarDiv('listadoGeneral',true);
    mostrarDiv('listadoIndividual',false);
    consultaGeneral();
}
function mostrarTitulo(titulo){
    document.getElementById("titulo").innerHTML="<h3>"+titulo+"</h3>";
}
function nuevo(){
    operacion='i';
    //consultarId();
    mostrarTitulo("Registro de Opciones");
    mostrarDiv("listadoIndividual",true);
    mostrarDiv("listadoGeneral",false);
    limpiarControles();
}
function editar(id){
    operacion='u';
    consultaIndividual(id);
    mostrarTitulo("Edicion de Opciones");
    mostrarDiv("listadoIndividual",true);
    mostrarDiv("listadoGeneral",false);
}
function eliminar(id){
    operacion='d';
    consultaIndividual(id);
    mostrarTitulo("Eliminacion de Opciones");
    mostrarDiv("listadoIndividual",true);
    mostrarDiv("listadoGeneral",false);
}
function consultaGeneral(){
    var ajax=new XMLHttpRequest();
    ajax.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            llenarTabla(this.responseText);
        }
    };
    ajax.open("get","/opciones/consultaGeneral",true);
    ajax.send();
}
function llenarTabla(respuesta){
    var datos=JSON.parse(respuesta);
    limpiarTabla();
    var table=document.getElementById("datos");
    for(i=0;i<datos.length;i++){
        var tr=document.createElement("tr");
        var opcion=datos[i];
        for(propiedad in opcion){
            var td=document.createElement("td");
            var text=document.createTextNode(opcion[propiedad]);
            td.appendChild(text);
            tr.appendChild(td);
        }
        table.appendChild(tr);
        var td=document.createElement("td");
        td.appendChild(crearLink(opcion.idOpcion, "editar"));
        tr.appendChild(td);
        table.appendChild(tr);
        td=document.createElement("td");
        td.appendChild(crearLink(opcion.idOpcion, "eliminar"));
        tr.appendChild(td);
        table.appendChild(tr);
    }
}
function crearLink(id,operacion){
	var link=document.createElement("a");
	link.setAttribute("href", "javascript:"+operacion+"("+id+")");
	var img=document.createElement("img");
	img.setAttribute("src", "static/imagenes/"+operacion+".png");
	link.appendChild(img);
	return link;
}
function limpiarTabla(){
	var table=document.getElementById("datos");
	for(i=table.rows.length-1;i>0;i--){
		table.removeChild(table.rows[i]);
	}
}
function aceptar(){
    var o={idOpcion:document.getElementById("id").value,
            nombre:document.getElementById("nombre").value,
            descripcion:document.getElementById("descripcion").value
          };
    var json=JSON.stringify(o);
    switch(operacion){
        case "i":
            insertar(json);
            break;
        case "u":
            modificarOpcion(json);
            break;
        case "d":
            if(confirm('¿Estas seguro de eliminar la opción '+o.nombre+' ?'))
                eliminarOpcion(o.idOpcion);
            break;
    }
    
}
function insertar(json){
    var url="/opciones/guardar/"+encodeURI(json);
    var ajax=new XMLHttpRequest();
    ajax.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            alert(this.responseText);
            inicializarDivs()
        }
    };
    ajax.open("get",url,true);
    ajax.send();
}
function modificarOpcion(json){
    var url="/opciones/modificar/"+encodeURI(json);
    var ajax=new XMLHttpRequest();
    ajax.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            alert(this.responseText);
            inicializarDivs()
        }
    };
    ajax.open("get",url,true);
    ajax.send();
}
function eliminarOpcion(id){
    var url="/opciones/delete/"+id;
    var ajax=new XMLHttpRequest();
    ajax.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            alert(this.responseText);
            inicializarDivs()
        }
    };
    ajax.open("get",url,true);
    ajax.send();
}
function consultaIndividual(id){
    var url="/opciones/"+id;
    var ajax=new XMLHttpRequest();
    ajax.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            llenarCampos(this.responseText);
        }
    };
    ajax.open("get",url,true);
    ajax.send();
}
function llenarCampos(respuesta){
	var obj=JSON.parse(respuesta);
	document.getElementById("id").value=obj.idOpcion;
    document.getElementById("nombre").value=obj.nombre;
    document.getElementById("descripcion").value=obj.descripcion;
}
function limpiarControles(){
	document.getElementById("id").value='';
    document.getElementById("nombre").value='';
    document.getElementById("descripcion").value='';
}
