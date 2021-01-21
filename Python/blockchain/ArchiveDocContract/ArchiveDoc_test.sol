pragma solidity >=0.4.22 <0.7.0;
import "remix_tests.sol"; // this import is automatically injected by Remix.
import "./ArchiveDoc.sol";

contract ArchiveDocTest {

    ArchiveDoc archiveDocTest;

    bytes32 docHash;
    bytes32[] docHashs;

    function beforeAll () public {
        docHash = 0x5a4607f7c641eb1e0e450ae75a1216e0f1e20cf1d996f574a36dfde145f1b862;
        docHashs.push(0x19fe9486e97d312037e0f49b89d4b3e38603229e0859f97a174307983c424fd3);
        docHashs.push(0x0e827559c9f9311beec5d9b6a41befc9ab0ab516a43000541ba42b8dd51bc84f);
        docHashs.push(0xa2250c6d18d8132033694a7d9d32888ef0e7a1490da40993bc95197edfe0d8f7);
        archiveDocTest = new ArchiveDoc();
    }

    function testSample () public {
        uint sum = 1 + 2;
        Assert.equal(3, sum, "sum is not 3");
    }

    function testAddHash () public {
        Assert.equal(archiveDocTest.isExist(docHash), false, "hash should not exist");

        archiveDocTest.addHash(docHash);

        Assert.equal(archiveDocTest.isExist(docHash), true, "hash should exist");
    }

    function testAddMultipleHash () public {
        for(uint i = 0; i < docHashs.length; i++){
            Assert.equal(archiveDocTest.isExist(docHashs[i]), false, "hash should not exist");
        }

        archiveDocTest.addMultipleHash(docHashs);

        for(uint i = 0; i < docHashs.length; i++){
            Assert.equal(archiveDocTest.isExist(docHashs[i]), true, "hash should exist");
        }

    }
}
