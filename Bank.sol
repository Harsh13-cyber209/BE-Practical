// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank{
    
    uint256 balance=0;
    address public accOwner;

    constructor(){
        accOwner=msg.sender;   
    }

    function Deposit() public payable {
        require(accOwner==msg.sender,"You're not a account owner");
        require(msg.value>0, "Amount should be greater than zero");
        balance+=msg.value;
    }
    function Withdraw() public payable {
        require(accOwner==msg.sender,"You're not a account owner");
        require(msg.value>0, "Please enter amount greater than zero");
        balance-=msg.value;
    }
    function ShowBalance() public view returns(uint256){
        require(accOwner==msg.sender,"You're not a account owner");
        return balance;

    }
}