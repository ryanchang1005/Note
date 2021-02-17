pragma solidity ^0.5.14;

contract Ownable {
  address public owner;

  constructor() public {
    owner = msg.sender;
  }

  modifier onlyOwner() {
    require(msg.sender == owner);
    _;
  }
}

interface Token {
  function balanceOf(address _owner) external pure returns (uint256 );
  function transfer(address _to, uint256 _value) external ;
  event Transfer(address indexed _from, address indexed _to, uint256 _value);
}

contract Airdropper is Ownable {
    function AirTransfer(address[] memory _recipients, uint _value, address _tokenAddress) onlyOwner public returns (bool) {
        require(_recipients.length > 0);

        Token token = Token(_tokenAddress);

        for(uint j = 0; j < _recipients.length; j++){
            token.transfer(_recipients[j], _value);
        }

        return true;
    }
}