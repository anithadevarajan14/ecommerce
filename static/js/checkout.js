$(document).ready(function() {
    $('.payWithRazorypay').click(function(e){
        e.preventDefault();

        var name = $("[name='name'] ").val();
        var lname = $("[name='lname'] ").val();
        var email = $("[name='email'] ").val();
        var phone = $("[name='phone'] ").val();
        var address = $("[name='address'] ").val();
        var city = $("[name='city'] ").val();
        var state = $("[name='state'] ").val();
        var country = $("[name='country'] ").val();
        var pincode = $("[name='pincode'] ").val();
        var token = $("[name='csrfmiddlewaretoken'] ").val();
        
        if(name=="" || lname == "" || email =="" || phone == "" || address =="" || city == "" || state =="" || country == "" || pincode =="" )
        {
            alert("");
            swal("Alert!", "All fields are mandatory", "error");
            return false;
        }
        else  
        {
            $.ajax({
                method: "GET",
                url:"/proceed-to-pay",
                success:function(response){
                    //console.log(response);
                    var options = {
                        "key":  "rzp_test_gaP3UhD2fGx38m",        
                        "amount": 1*100, 
                        "currency": "INR",
                        "name": "Shopkart", 
                        "description": "Thank you for buying from us",
                        //"order_id": "razorpay_order_id", 
                        "handler": function(responseb){
                            alert(responseb.razorpay_payment_id); 
                            data = {
                                "name" : name ,
                                lname :'lname',
                                email :'email',
                                phone :'phone',
                                address : 'address',
                                city :'city',
                                state : 'state',
                                country : 'country',
                                pincode : 'pincode',
                                "payment_mode": 'Paid by Razorpay',
                                "payment_id": responseb.razorpay_payment_id,
                                csrfmiddlewaretoken : token
                            }
                            $.ajax({
                                method:"POST",
                                url:"/place-order",
                                data :data,
                                success: function(response){
                                    swal("Congratulations!", responsec.status, "success").then((value)=>{
                                        window.location.href ='/'
                                    });
                                    
                                }


                            });

                        },
                        "prefill":{
                            "name": name + " " + lname,
                            "email": email,
                            "contact": phone                                                  
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            });

        }  
    
     
    });
});