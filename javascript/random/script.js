const myButton=document.getElementById("myButton")
const label1=document.getElementById("label1")
const label2=document.getElementById("label2")
const label3=document.getElementById("label3")

const maxi=50
const mini=10

myButton.onclick=function(){
    label1.textContent=Math.floor(Math.random() * maxi)+ mini
    label2.textContent=Math.floor(Math.random() * maxi)+ mini
    label3.textContent=Math.floor(Math.random() * maxi)+ mini
}