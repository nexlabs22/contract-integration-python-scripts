tokenAbi = [
    {
       "inputs": [
          {
             "internalType": "uint256",
             "name": "initialSupply",
             "type": "uint256"
          },
          {
             "internalType": "string",
             "name": "_name",
             "type": "string"
          },
          {
             "internalType": "string",
             "name": "_symbol",
             "type": "string"
          }
       ],
       "stateMutability": "nonpayable",
       "type": "constructor"
    },
    {
       "anonymous": False,
       "inputs": [
          {
             "indexed": True,
             "internalType": "address",
             "name": "owner",
             "type": "address"
          },
          {
             "indexed": True,
             "internalType": "address",
             "name": "spender",
             "type": "address"
          },
          {
             "indexed": False,
             "internalType": "uint256",
             "name": "value",
             "type": "uint256"
          }
       ],
       "name": "Approval",
       "type": "event"
    },
    {
       "anonymous": False,
       "inputs": [
          {
             "indexed": True,
             "internalType": "address",
             "name": "from",
             "type": "address"
          },
          {
             "indexed": True,
             "internalType": "address",
             "name": "to",
             "type": "address"
          },
          {
             "indexed": False,
             "internalType": "uint256",
             "name": "value",
             "type": "uint256"
          }
       ],
       "name": "Transfer",
       "type": "event"
    },
    {
       "inputs": [
          {
             "internalType": "address",
             "name": "owner",
             "type": "address"
          },
          {
             "internalType": "address",
             "name": "spender",
             "type": "address"
          }
       ],
       "name": "allowance",
       "outputs": [
          {
             "internalType": "uint256",
             "name": "",
             "type": "uint256"
          }
       ],
       "stateMutability": "view",
       "type": "function"
    },
    {
       "inputs": [
          {
             "internalType": "address",
             "name": "spender",
             "type": "address"
          },
          {
             "internalType": "uint256",
             "name": "amount",
             "type": "uint256"
          }
       ],
       "name": "approve",
       "outputs": [
          {
             "internalType": "bool",
             "name": "",
             "type": "bool"
          }
       ],
       "stateMutability": "nonpayable",
       "type": "function"
    },
    {
       "inputs": [
          {
             "internalType": "address",
             "name": "account",
             "type": "address"
          }
       ],
       "name": "balanceOf",
       "outputs": [
          {
             "internalType": "uint256",
             "name": "",
             "type": "uint256"
          }
       ],
       "stateMutability": "view",
       "type": "function"
    },
    {
       "inputs": [],
       "name": "decimals",
       "outputs": [
          {
             "internalType": "uint8",
             "name": "",
             "type": "uint8"
          }
       ],
       "stateMutability": "view",
       "type": "function"
    },
    {
       "inputs": [
          {
             "internalType": "address",
             "name": "spender",
             "type": "address"
          },
          {
             "internalType": "uint256",
             "name": "subtractedValue",
             "type": "uint256"
          }
       ],
       "name": "decreaseAllowance",
       "outputs": [
          {
             "internalType": "bool",
             "name": "",
             "type": "bool"
          }
       ],
       "stateMutability": "nonpayable",
       "type": "function"
    },
    {
       "inputs": [
          {
             "internalType": "address",
             "name": "spender",
             "type": "address"
          },
          {
             "internalType": "uint256",
             "name": "addedValue",
             "type": "uint256"
          }
       ],
       "name": "increaseAllowance",
       "outputs": [
          {
             "internalType": "bool",
             "name": "",
             "type": "bool"
          }
       ],
       "stateMutability": "nonpayable",
       "type": "function"
    },
    {
       "inputs": [],
       "name": "name",
       "outputs": [
          {
             "internalType": "string",
             "name": "",
             "type": "string"
          }
       ],
       "stateMutability": "view",
       "type": "function"
    },
    {
       "inputs": [],
       "name": "symbol",
       "outputs": [
          {
             "internalType": "string",
             "name": "",
             "type": "string"
          }
       ],
       "stateMutability": "view",
       "type": "function"
    },
    {
       "inputs": [],
       "name": "totalSupply",
       "outputs": [
          {
             "internalType": "uint256",
             "name": "",
             "type": "uint256"
          }
       ],
       "stateMutability": "view",
       "type": "function"
    },
    {
       "inputs": [
          {
             "internalType": "address",
             "name": "to",
             "type": "address"
          },
          {
             "internalType": "uint256",
             "name": "amount",
             "type": "uint256"
          }
       ],
       "name": "transfer",
       "outputs": [
          {
             "internalType": "bool",
             "name": "",
             "type": "bool"
          }
       ],
       "stateMutability": "nonpayable",
       "type": "function"
    },
    {
       "inputs": [
          {
             "internalType": "address",
             "name": "from",
             "type": "address"
          },
          {
             "internalType": "address",
             "name": "to",
             "type": "address"
          },
          {
             "internalType": "uint256",
             "name": "amount",
             "type": "uint256"
          }
       ],
       "name": "transferFrom",
       "outputs": [
          {
             "internalType": "bool",
             "name": "",
             "type": "bool"
          }
       ],
       "stateMutability": "nonpayable",
       "type": "function"
    }
 ]

indexTokenAbi = [
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "feeRatePerDayScaled",
          "type": "uint256"
        }
      ],
      "name": "FeeRateSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "feeReceiver",
          "type": "address"
        }
      ],
      "name": "FeeReceiverSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "version",
          "type": "uint8"
        }
      ],
      "name": "Initialized",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "methodologist",
          "type": "address"
        }
      ],
      "name": "MethodologistSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "string",
          "name": "methodology",
          "type": "string"
        }
      ],
      "name": "MethodologySet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "feeReceiver",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "totalSupply",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "MintFeeToReceiver",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "minter",
          "type": "address"
        }
      ],
      "name": "MinterSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Paused",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "supplyCeiling",
          "type": "uint256"
        }
      ],
      "name": "SupplyCeilingSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "isRestricted",
          "type": "bool"
        }
      ],
      "name": "ToggledRestricted",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Unpaused",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        }
      ],
      "name": "allowance",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "burn",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "decimals",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "subtractedValue",
          "type": "uint256"
        }
      ],
      "name": "decreaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "feeRatePerDayScaled",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "feeReceiver",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "feeTimestamp",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "addedValue",
          "type": "uint256"
        }
      ],
      "name": "increaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "tokenName",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "tokenSymbol",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "_feeRatePerDayScaled",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "_feeReceiver",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_supplyCeiling",
          "type": "uint256"
        }
      ],
      "name": "initialize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "isRestricted",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "methodologist",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "methodology",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "mint",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "mintToFeeReceiver",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "minter",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "paused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_proposedOwner",
          "type": "address"
        }
      ],
      "name": "proposeOwner",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "proposedOwner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_feeRatePerDayScaled",
          "type": "uint256"
        }
      ],
      "name": "setFeeRate",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_feeReceiver",
          "type": "address"
        }
      ],
      "name": "setFeeReceiver",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_methodologist",
          "type": "address"
        }
      ],
      "name": "setMethodologist",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_methodology",
          "type": "string"
        }
      ],
      "name": "setMethodology",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_minter",
          "type": "address"
        }
      ],
      "name": "setMinter",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_supplyCeiling",
          "type": "uint256"
        }
      ],
      "name": "setSupplyCeiling",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "supplyCeiling",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "who",
          "type": "address"
        }
      ],
      "name": "toggleRestriction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "unpause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]

factoryAbi = [
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "inputRequestHash",
          "type": "bytes32"
        }
      ],
      "name": "BurnConfirmed",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "name": "Burned",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "custodian",
          "type": "address"
        }
      ],
      "name": "CustodianSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "version",
          "type": "uint8"
        }
      ],
      "name": "Initialized",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "merchant",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        }
      ],
      "name": "IssuerDepositAddressSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "issuer",
          "type": "address"
        }
      ],
      "name": "IssuerSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "merchant",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        }
      ],
      "name": "MerchantDepositAddressSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "name": "MintConfirmed",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "name": "MintRejected",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "name": "MintRequestAdd",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "name": "MintRequestCancel",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Paused",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "time",
          "type": "uint256"
        }
      ],
      "name": "TokenAddressSet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Unpaused",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "usdc",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint8",
          "name": "decimals",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "time",
          "type": "uint256"
        }
      ],
      "name": "UsdcAddressSet",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "addMintRequest",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "burn",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "name": "burnRequestNonce",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "burnRequests",
      "outputs": [
        {
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "internalType": "enum IndexFactoryInterface.RequestStatus",
          "name": "status",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "name": "confirmBurnRequest",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        },
        {
          "internalType": "uint256",
          "name": "_tokenAmount",
          "type": "uint256"
        }
      ],
      "name": "confirmMintRequest",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "custodianWallet",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getAllBurnRequests",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "requester",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "amount",
              "type": "uint256"
            },
            {
              "internalType": "address",
              "name": "depositAddress",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "nonce",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "timestamp",
              "type": "uint256"
            },
            {
              "internalType": "enum IndexFactoryInterface.RequestStatus",
              "name": "status",
              "type": "uint8"
            }
          ],
          "internalType": "struct IndexFactoryInterface.Request[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getAllMintRequests",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address",
              "name": "requester",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "amount",
              "type": "uint256"
            },
            {
              "internalType": "address",
              "name": "depositAddress",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "nonce",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "timestamp",
              "type": "uint256"
            },
            {
              "internalType": "enum IndexFactoryInterface.RequestStatus",
              "name": "status",
              "type": "uint8"
            }
          ],
          "internalType": "struct IndexFactoryInterface.Request[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        }
      ],
      "name": "getBurnRequest",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "requestNonce",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "status",
          "type": "string"
        },
        {
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getBurnRequestsLength",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "length",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        }
      ],
      "name": "getMintRequest",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "requestNonce",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "status",
          "type": "string"
        },
        {
          "internalType": "bytes32",
          "name": "requestHash",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getMintRequestsLength",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "length",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_custodianWallet",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_issuer",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_token",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "_usdc",
          "type": "address"
        },
        {
          "internalType": "uint8",
          "name": "_usdcDecimals",
          "type": "uint8"
        }
      ],
      "name": "initialize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "issuer",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "name": "mintRequestNonce",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "mintRequests",
      "outputs": [
        {
          "internalType": "address",
          "name": "requester",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "depositAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "internalType": "enum IndexFactoryInterface.RequestStatus",
          "name": "status",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "paused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_custodianWallet",
          "type": "address"
        }
      ],
      "name": "setCustodianWallet",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_issuer",
          "type": "address"
        }
      ],
      "name": "setIssuer",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_token",
          "type": "address"
        }
      ],
      "name": "setTokenAddress",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_usdc",
          "type": "address"
        },
        {
          "internalType": "uint8",
          "name": "_usdcDecimals",
          "type": "uint8"
        }
      ],
      "name": "setUsdcAddress",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "token",
      "outputs": [
        {
          "internalType": "contract IndexToken",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "unpause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "usdc",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "usdcDecimals",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]