var cont=0;
function mostrarDiv(nombre){
    var otraVariable;
    otraVariable=5;
    var div=document.getElementById(nombre);
    div.style.display="block";
    otraVariable="Hola mundo";
    cont++;
}
function ocultarDiv(nombre){
   var div=document.getElementById(nombre); 
   //alert(div);
   div.style.display="none";
   if(cont>3)
    alert(cont);
   else
    alert('otra cosa');
}
function ocultarDivs(){
    
    ocultarDiv("datosEstructurales");
}
function mostrarAlumno(){
  var alumno={
    "nombre":"Juan",
    "promedio":70,
    "materias_acreditadas":[
        {
            "nombre_materia":"Español",
            "calificacion":70,
            "semestre":1
        },
        {
            "nombre_materia":"Matematicas",
            "calificacion":70,
            "semestre":1
        },
        {
            "nombre_materia":"Quimica",
            "calificacion":71,
            "semestre":1
        }
        
    ]  
  };
  alert("Nombre:"+alumno.nombre+" Promedio:"
  +alumno.promedio+
  " Materias:"+alumno.materias_acreditadas[0]+","
  +alumno.materias_acreditadas[1]);
  /*
  for(i=0;i<alumno.materias_acreditadas.length;i++){
    alert(alumno.materias_acreditadas[i].nombre_materia
        +" "+alumno.materias_acreditadas[i].calificacion
        +" "+alumno.materias_acreditadas[i].semestre);
  }*/
  for(materia in alumno.materias_acreditadas)
    alert(alumno.materias_acreditadas[materia].nombre_materia);
  /*switch(alumno.promedio){
      case 70:
          alert("Debes mejorar");
          break;
      case 80:
          alert("Bien");
          break;
      case 90:
          alert('Muy bien');
          break;
      case 100:
          alert("Excelente");
          break;            
  }
  switch(alumno.materias_acreditadas[0]){
      case "Español":
          alert("Español");
          break;
      case "Matematicas":
          alert("Matematicas");  
          break;  
  }*/
}
/*
var miFuncion=ocultarDivs;
miFuncion();
*/
