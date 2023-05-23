var web3;
var address="0x33e69fB6eE3E1e8D57f737bDE10009a0D83E7768";

var abi =[
	{
		"inputs": [
			{
				"internalType": "int256",
				"name": "amt",
				"type": "int256"
			}
		],
		"name": "deposite_money",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "int256",
				"name": "amt",
				"type": "int256"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
];
var contract=new web3.eth.Contract(abi,address);

function deposite(){
    var inputval=document.getElementById("amount").value;

    web3.eth.getAccounts().then(function(account){
        return contract.methods.deposite_money(inputval).send({from: account[0]});
    }).then(function(tmp){
        $("#amount").val("");
    }).catch(function(tmp){
        alert(tmp);
    })
}