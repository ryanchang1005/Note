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

contract AuditDoc is Ownable, StaffRole {
    struct Auditor {
        address auditor;
        bool isAudit;
        string hash;
    }
    struct Doc {
        string docId;
        mapping(uint256 => Auditor) auditors;
        uint256 auditorsCount;
        bool exists;
    }
    mapping(string => Doc) public docs;

    mapping(uint256 => Auditor) emptyMap;

    event AddDoc(string _docId, address[] _auditors);

    function addDoc(string memory _docId, address[] memory _auditors)
        public
        onlyStaff
    {
        require(!isDocExist(_docId), "doc already exist");
        Doc storage doc = docs[_docId];
        doc.docId = _docId;
        doc.exists = true;
        doc.auditorsCount = 0;
        
        for (uint256 i = 0; i < _auditors.length; i++) {
            require(isStaff(_auditors[i]), "some one not staff");
            
            Auditor memory it;
            it.auditor = _auditors[i];
            it.isAudit = false;
            it.hash = "";
            doc.auditors[i] = it;
            doc.auditorsCount++;
        }
        emit AddDoc(_docId, _auditors);
    }

    function isDocExist(string memory _docId) public view returns (bool) {
        return docs[_docId].exists;
    }

    function auditorCount(string memory _docId) public view returns (uint256) {
        if (!isDocExist(_docId)) {
            return 0;
        }
        return docs[_docId].auditorsCount;
    }

    function isDocFinish(string memory _docId) public view returns (bool) {
        if (!isDocExist(_docId)) {
            return false;
        }
        for (uint256 i = 0; i < docs[_docId].auditorsCount; i++) {
            if (docs[_docId].auditors[i].isAudit == false) {
                return false;
            }
        }
        return true;
    }

    event Audit(string _docId, address auditor, string _hash);

    function audit(string memory _docId, string memory _hash) public onlyStaff {
        require(isDocExist(_docId), "doc not exist");

        Doc storage doc = docs[_docId];
        for (uint256 i = 0; i < doc.auditorsCount; i++) {
            Auditor storage auditor = doc.auditors[i];
            if (auditor.auditor == msg.sender) {
                auditor.isAudit = true;
                auditor.hash = _hash;
                emit Audit(_docId, msg.sender, _hash);
                break;
            }
        }
    }

    function compareStrings(string memory a, string memory b)
        public
        pure
        returns (bool)
    {
        return (keccak256(abi.encodePacked((a))) ==
            keccak256(abi.encodePacked((b))));
    }

    function isAuditHashValid(
        string memory _docId,
        address _auditor,
        string memory _hash
    ) public view returns (bool) {
        require(isDocExist(_docId), "doc not exist");

        Doc storage doc = docs[_docId];
        for (uint256 i = 0; i < doc.auditorsCount; i++) {
            if (doc.auditors[i].auditor == _auditor) {
                return compareStrings(doc.auditors[i].hash, _hash);
            }
        }
        return false;
    }

    event InsertAuditor(string _docId, uint256 _position, address _auditor);

    function insertAuditor(
        string memory _docId,
        uint256 _position,
        address _auditor
    ) public onlyStaff {
        require(isDocExist(_docId), "doc not exist");

        // count total swap times(orgin length - position = swap step)
        uint256 swapTimes = docs[_docId].auditorsCount - _position;

        // add new Auditor to end
        Auditor memory it;
        it.auditor = _auditor;
        it.isAudit = false;
        it.hash = "";
        docs[_docId].auditors[docs[_docId].auditorsCount] = it;
        docs[_docId].auditorsCount++;

        // right index
        uint256 r = docs[_docId].auditorsCount - 1;
        for (uint256 i = 0; i < swapTimes; i++) {
            // swap
            Auditor memory tmp = docs[_docId].auditors[r];
            docs[_docId].auditors[r] = docs[_docId].auditors[r - 1];
            docs[_docId].auditors[r - 1] = tmp;

            // move index left one step
            r = r - 1;
        }

        emit InsertAuditor(_docId, _position, _auditor);
    }
}
