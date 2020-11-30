/*function Edificio1(id,nombre){
    this.id=id;
    this.nombre=nombre;
    this.mostrarDatos=function(){ 
        return "ID:"+this.id+", nombre:"+this.nombre;
    };
}  */ 
var arrayEdificios=[];
class Edificio{
    constructor(id,nombre) 
    {
        this.id=id;
        this.nombre=nombre;
    }
    toString() {
        return "ID:"+this.id+" ,nombre:"+this.nombre;
    }    
    guardar(){
        //Almacenará el objeto en la BD
        arrayEdificios.push(this)
    }
    actualizar(){
        for(i=0;i<arrayEdificios.length;i++){
            if(arrayEdificios[i].id==this.id){
                arrayEdificios[i]=this;
            }
        }
    }
    eliminar(){
        for(i=0;i<arrayEdificios.length;i++){
            if(arrayEdificios[i].id==this.id){
                //delete arrayEdificios[i];
                arrayEdificios.splice(i,1);
            }
        } 
    }
    consultar(){
        for(i=0;i<arrayEdificios.length;i++){
            if(arrayEdificios[i].id==this.id){
                return arrayEdificios[i];
            }
        }
        return null;
    }
}  
