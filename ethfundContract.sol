//SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.5.0 < 0.9.0;

contract ethfund{

    mapping(address=>uint) public investors; //investors[msg.sender]=100
    address public creator;

    uint public deadline;
    uint public target;
    
    struct Request{
        string description;
        address payable recipient;
        uint value;
        bool completed;
        uint noOfVoters;
        mapping(address=>bool) voters;
    }

    uint public raisedAmount;
    uint public noOfInvestors;

    mapping(uint=>Request) public requests;
    uint public numRequests;
    
    constructor(uint _target,uint _deadline){
        target=_target;
        deadline=block.timestamp+_deadline*24*60*60; //10sec + 3600sec (60*60)
        creator=msg.sender;
    }
    
    function sendEth() public payable{
        require(block.timestamp < deadline,"Deadline has passed");
        if(investors[msg.sender]==0){
            noOfInvestors++;
        }
        investors[msg.sender]+=msg.value;
        raisedAmount+=msg.value;
    }

    function getContractBalance() public view returns(uint){
        return address(this).balance;
    }

    function getcreatorValue() public view returns (address){
        return creator;
    }

    function getDeadlineValue() public view returns (uint){
        return deadline;
    }

    function getTargetValue() public view returns (uint){
        return target;
    }

    function getRaisedAmountValue() public view returns (uint){
        return raisedAmount;
    }

    function getnoOfInvestors() public view returns (uint){
        return noOfInvestors;
    }

    function getnumRequests() public view returns (uint){
        return numRequests;
    }

    function refund() public{
        require(block.timestamp>deadline && raisedAmount<target,"You are not eligible for refund");
        require(investors[msg.sender]>0);
        address payable user=payable(msg.sender);
        user.transfer(investors[msg.sender]);
        investors[msg.sender]=0;
    }

    modifier onlyCreator(){
        require(msg.sender==creator,"Only creator can calll this function");
        _;
    }

    function createRequests(string memory _description,address payable _recipient,uint _value) public onlyCreator{
        Request storage newRequest = requests[numRequests];
        numRequests++;
        newRequest.description=_description;
        newRequest.recipient=_recipient;
        newRequest.value=_value;
        newRequest.completed=false;
        newRequest.noOfVoters=0;
    }

    function voteRequest(uint _requestNo) public{
        require(investors[msg.sender]>0,"You must be contributor");
        Request storage thisRequest=requests[_requestNo];
        require(thisRequest.voters[msg.sender]==false,"You have already voted");
        thisRequest.voters[msg.sender]=true;
        thisRequest.noOfVoters++;
    }

    function makePayment(uint _requestNo) public onlyCreator{
        require(raisedAmount>=target);
        Request storage thisRequest=requests[_requestNo];
        require(thisRequest.completed==false,"The request has been completed");
        require(thisRequest.noOfVoters > noOfInvestors/2,"Majority does not support");
        thisRequest.recipient.transfer(thisRequest.value);
        thisRequest.completed=true;
    }

}
