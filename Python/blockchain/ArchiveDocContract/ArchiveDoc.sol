pragma solidity >=0.4.22 <0.7.0;

contract Ownable {
    address private _owner;

    /**
     * @dev Initializes the contract setting the deployer as the initial owner.
     */
    constructor () internal {
        _owner = msg.sender;
        emit OwnershipTransferred(address(0), _owner);
    }

    /**
     * @dev Returns the address of the current owner.
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Throws if called by any account other than the owner.
     */
    modifier onlyOwner() {
        require(isOwner(), "Ownable: caller is not the owner");
        _;
    }

    /**
     * @dev Returns true if the caller is the current owner.
     */
    function isOwner() public view returns (bool) {
        return msg.sender == _owner;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        _owner = newOwner;
        emit OwnershipTransferred(_owner, newOwner);
    }

    event OwnershipTransferred(address _previousOwner, address _newOwner);
}

contract StaffRole is Ownable {
    mapping (address => bool) staffs;

    constructor () internal {
        addStaff(msg.sender);
    }

    modifier onlyStaff() {
        require(isStaff(msg.sender), "StaffRole: caller does not have the staff role");
        _;
    }

    function addStaff(address _address) public onlyOwner {
        staffs[_address] = true;
        emit AddStaff(_address);
    }

    function removeStaff(address _address) public onlyOwner {
        require(isStaff(_address), "StaffRole: address does not have role");
        staffs[_address] = false;
        emit RemoveStaff(_address);
    }

    function isStaff(address _address) public view returns (bool) {
        return staffs[_address];
    }
    
    event AddStaff(address _address);
    event RemoveStaff(address _address);
}

contract ArchiveDoc is Ownable, StaffRole {
    mapping (bytes32 => bool) hashExists;

    event AddHash(bytes32 hash);

    function addHash(bytes32 hash) public onlyStaff {
        require(!isExist(hash), "ArchiveDoc: hash already exist");
        hashExists[hash] = true;
        emit AddHash(hash);
    }

    function addMultipleHash(bytes32[] memory hashs) public onlyStaff {
        for(uint i = 0; i < hashs.length; i++){
            require(!isExist(hashs[i]), "ArchiveDoc: hash already exist");
        }

        for(uint i = 0; i < hashs.length; i++){
            hashExists[hashs[i]] = true;
            emit AddHash(hashs[i]);
        }
    }
    
    function isExist(bytes32 hash) public view returns (bool) {
        return hashExists[hash];
    }
}