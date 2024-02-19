//  comentario de mais de um linha usa / * e precisa fechar com */ ou usar cltr e a barra
// funçoes ->function nome da função (){}
// pareteci é para declara paramentros na função
/*
function soma(a,b){
    console.log(a+b);//serve pra imprimir no console
    return a+b;
}

soma(3,5);//chama a função e é necessario passar os paramentros

*/
function returnEvenValues(array){
   let evenNums=[];
    for(let i=0;i<array.length;i++){
    if(array[i]%2==0){
        evenNums.push(array[i]);
        }
    }
    console.log('os numeros pares são: ',evenNums);
}


let teste = [1,2,4,5,7,8];
returnEvenValues(teste);