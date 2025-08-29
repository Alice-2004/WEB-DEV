const checkbox=document.getElementById("checkbox")
const visa=document.getElementById("visa")
const mastercard=document.getElementById("master")
const PayPal=document.getElementById("paypal")
const submit=document.getElementById("submit")
const sub=document.getElementById("sub")
const pay=document.getElementById("pay")

submit.onclick=function(){
    if(checkbox.checked){
        sub.textContent=`You are subscribed !`
    }
    else{
        sub.textContent=`You are NOT subscribed !`
    }
    if(visa.checked){
        pay.textContent=`Payment is through visa card`
    }
    else if(mastercard.checked){
        pay.textContent=`Payment is through master card`
    }
    else if(PayPal.checked){
        pay.textContent=`Payment is through paypal`
    }
    else{
        pay.textContent=`Please do the payment`
    }
}
