pragma solidity >=0.4.22 <0.7.0;

contract Ownable {
    address private _owner;

    /**
     * @dev Initializes the contract setting the deployer as the initial owner.
     */
    constructor() internal {
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
        require(
            newOwner != address(0),
            "Ownable: new owner is the zero address"
        );
        _owner = newOwner;
        emit OwnershipTransferred(_owner, newOwner);
    }

    event OwnershipTransferred(address _previousOwner, address _newOwner);
}

contract StaffRole is Ownable {
    mapping(address => bool) staffs;

    constructor() internal {
        addStaff(msg.sender);
    }

    modifier onlyStaff() {
        require(
            isStaff(msg.sender),
            "StaffRole: caller does not have the staff role"
        );
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

contract MarkDocStatus is Ownable, StaffRole {
    struct Doc {
        string docId;
        uint8 status;
        bool isExist;
    }

    uint8 constant NONE = 0;
    uint8 constant VERIFY = 1;
    uint8 constant REFUSE = 2;
    uint8 constant REVOKE = 3;

    mapping(string => Doc) docs;

    function isDocExist(string memory _docId) public view returns (bool) {
        return docs[_docId].isExist;
    }

    event AddDoc(string _docId);

    function addDoc(string memory _docId) public onlyStaff {
        require(!isDocExist(_docId), "doc already exist");

        docs[_docId] = Doc({docId: _docId, status: 0, isExist: true});

        emit AddDoc(_docId);
    }

    event SetDocStatus(string _docId, uint8 status);

    function setDocStatus(string memory _docId, uint8 status) public onlyStaff {
        require(isDocExist(_docId), "doc should exist");
        if (status != VERIFY && status != REFUSE && status != REVOKE) {
            require(false, "status not allow");
        }

        if (docs[_docId].status != NONE) {
            require(false, "status not none");
        }

        docs[_docId].status = status;
        emit SetDocStatus(_docId, status);
    }

    function getDocStatus(string memory _docId) public view returns (uint8) {
        return docs[_docId].status;
    }
}
