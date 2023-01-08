pragma solidity ^0.4.0;
import "./ERC20.sol";

contract myToken is ERC20{
    mapping(address =>unit256) public amount;
    unit256 totalAmount;
    string tokeName;
    string tokeSymbol;
    unit256 decimal;
    constructor() public{
        totalAmount = 1000 * 10**18;
        amount[msg.sender]=totalAmount;
        tokenName="Mytoken";
        tokenSymbol="Mytoken";
        decimal=18;
    }
    function totalSupply() public view returns(unit256){
        return totalAmount;
    }
    function balanceOf(address_to_who) public view
    returns(unit256){
        return amount[_to_who];
    }
    function transfer(address to_a, unit256_value)
    public
    returns(bool){
        require(_value<=amount[msg.sender]);
        amount[msg.sender]=amount[msg.sender]-_value;
        amount[to_a]=amount[to_a]+_value;
        return true;
    }
}