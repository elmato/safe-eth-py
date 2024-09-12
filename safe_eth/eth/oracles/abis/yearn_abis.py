# https://etherscan.io/address/0x03403154afc09Ce8e44C3B185C82C6aD5f86b9ab
YVAULT_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "_token", "type": "address"},
            {"internalType": "address", "name": "_controller", "type": "address"},
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "constant": True,
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "available",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "balance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "controller",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
        ],
        "name": "decreaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "deposit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [],
        "name": "depositAll",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [],
        "name": "earn",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getPricePerFullShare",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "governance",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
        ],
        "name": "increaseAllowance",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "max",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "min",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "_controller", "type": "address"}
        ],
        "name": "setController",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "_governance", "type": "address"}
        ],
        "name": "setGovernance",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"internalType": "uint256", "name": "_min", "type": "uint256"}],
        "name": "setMin",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"internalType": "string", "name": "_name", "type": "string"}],
        "name": "setName",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"internalType": "string", "name": "_symbol", "type": "string"}],
        "name": "setSymbol",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "token",
        "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"internalType": "uint256", "name": "_shares", "type": "uint256"}],
        "name": "withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [],
        "name": "withdrawAll",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

YTOKEN_ABI = [
    {
        "name": "Transfer",
        "inputs": [
            {"name": "sender", "type": "address", "indexed": True},
            {"name": "receiver", "type": "address", "indexed": True},
            {"name": "value", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "Approval",
        "inputs": [
            {"name": "owner", "type": "address", "indexed": True},
            {"name": "spender", "type": "address", "indexed": True},
            {"name": "value", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyAdded",
        "inputs": [
            {"name": "strategy", "type": "address", "indexed": True},
            {"name": "debtRatio", "type": "uint256", "indexed": False},
            {"name": "minDebtPerHarvest", "type": "uint256", "indexed": False},
            {"name": "maxDebtPerHarvest", "type": "uint256", "indexed": False},
            {"name": "performanceFee", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyReported",
        "inputs": [
            {"name": "strategy", "type": "address", "indexed": True},
            {"name": "gain", "type": "uint256", "indexed": False},
            {"name": "loss", "type": "uint256", "indexed": False},
            {"name": "debtPaid", "type": "uint256", "indexed": False},
            {"name": "totalGain", "type": "uint256", "indexed": False},
            {"name": "totalLoss", "type": "uint256", "indexed": False},
            {"name": "totalDebt", "type": "uint256", "indexed": False},
            {"name": "debtAdded", "type": "uint256", "indexed": False},
            {"name": "debtRatio", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateGovernance",
        "inputs": [{"name": "governance", "type": "address", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateManagement",
        "inputs": [{"name": "management", "type": "address", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateGuestList",
        "inputs": [{"name": "guestList", "type": "address", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateRewards",
        "inputs": [{"name": "rewards", "type": "address", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateDepositLimit",
        "inputs": [{"name": "depositLimit", "type": "uint256", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdatePerformanceFee",
        "inputs": [{"name": "performanceFee", "type": "uint256", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateManagementFee",
        "inputs": [{"name": "managementFee", "type": "uint256", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateGuardian",
        "inputs": [{"name": "guardian", "type": "address", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "EmergencyShutdown",
        "inputs": [{"name": "active", "type": "bool", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "UpdateWithdrawalQueue",
        "inputs": [{"name": "queue", "type": "address[20]", "indexed": False}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyUpdateDebtRatio",
        "inputs": [
            {"name": "strategy", "type": "address", "indexed": True},
            {"name": "debtRatio", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyUpdateMinDebtPerHarvest",
        "inputs": [
            {"name": "strategy", "type": "address", "indexed": True},
            {"name": "minDebtPerHarvest", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyUpdateMaxDebtPerHarvest",
        "inputs": [
            {"name": "strategy", "type": "address", "indexed": True},
            {"name": "maxDebtPerHarvest", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyUpdatePerformanceFee",
        "inputs": [
            {"name": "strategy", "type": "address", "indexed": True},
            {"name": "performanceFee", "type": "uint256", "indexed": False},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyMigrated",
        "inputs": [
            {"name": "oldVersion", "type": "address", "indexed": True},
            {"name": "newVersion", "type": "address", "indexed": True},
        ],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyRevoked",
        "inputs": [{"name": "strategy", "type": "address", "indexed": True}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyRemovedFromQueue",
        "inputs": [{"name": "strategy", "type": "address", "indexed": True}],
        "anonymous": False,
        "type": "event",
    },
    {
        "name": "StrategyAddedToQueue",
        "inputs": [{"name": "strategy", "type": "address", "indexed": True}],
        "anonymous": False,
        "type": "event",
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "initialize",
        "inputs": [
            {"name": "token", "type": "address"},
            {"name": "governance", "type": "address"},
            {"name": "rewards", "type": "address"},
            {"name": "nameOverride", "type": "string"},
            {"name": "symbolOverride", "type": "string"},
        ],
        "outputs": [],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "initialize",
        "inputs": [
            {"name": "token", "type": "address"},
            {"name": "governance", "type": "address"},
            {"name": "rewards", "type": "address"},
            {"name": "nameOverride", "type": "string"},
            {"name": "symbolOverride", "type": "string"},
            {"name": "guardian", "type": "address"},
        ],
        "outputs": [],
    },
    {
        "stateMutability": "pure",
        "type": "function",
        "name": "apiVersion",
        "inputs": [],
        "outputs": [{"name": "", "type": "string"}],
        "gas": 4546,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setName",
        "inputs": [{"name": "name", "type": "string"}],
        "outputs": [],
        "gas": 107044,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setSymbol",
        "inputs": [{"name": "symbol", "type": "string"}],
        "outputs": [],
        "gas": 71894,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setGovernance",
        "inputs": [{"name": "governance", "type": "address"}],
        "outputs": [],
        "gas": 36365,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "acceptGovernance",
        "inputs": [],
        "outputs": [],
        "gas": 37637,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setManagement",
        "inputs": [{"name": "management", "type": "address"}],
        "outputs": [],
        "gas": 37775,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setGuestList",
        "inputs": [{"name": "guestList", "type": "address"}],
        "outputs": [],
        "gas": 37805,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setRewards",
        "inputs": [{"name": "rewards", "type": "address"}],
        "outputs": [],
        "gas": 37835,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setLockedProfitDegration",
        "inputs": [{"name": "degration", "type": "uint256"}],
        "outputs": [],
        "gas": 36519,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setDepositLimit",
        "inputs": [{"name": "limit", "type": "uint256"}],
        "outputs": [],
        "gas": 37795,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setPerformanceFee",
        "inputs": [{"name": "fee", "type": "uint256"}],
        "outputs": [],
        "gas": 37929,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setManagementFee",
        "inputs": [{"name": "fee", "type": "uint256"}],
        "outputs": [],
        "gas": 37959,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setGuardian",
        "inputs": [{"name": "guardian", "type": "address"}],
        "outputs": [],
        "gas": 39203,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setEmergencyShutdown",
        "inputs": [{"name": "active", "type": "bool"}],
        "outputs": [],
        "gas": 39274,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "setWithdrawalQueue",
        "inputs": [{"name": "queue", "type": "address[20]"}],
        "outputs": [],
        "gas": 763950,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "transfer",
        "inputs": [
            {"name": "receiver", "type": "address"},
            {"name": "amount", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "bool"}],
        "gas": 76768,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "transferFrom",
        "inputs": [
            {"name": "sender", "type": "address"},
            {"name": "receiver", "type": "address"},
            {"name": "amount", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "bool"}],
        "gas": 116531,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "approve",
        "inputs": [
            {"name": "spender", "type": "address"},
            {"name": "amount", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "bool"}],
        "gas": 38271,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "increaseAllowance",
        "inputs": [
            {"name": "spender", "type": "address"},
            {"name": "amount", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "bool"}],
        "gas": 40312,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "decreaseAllowance",
        "inputs": [
            {"name": "spender", "type": "address"},
            {"name": "amount", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "bool"}],
        "gas": 40336,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "permit",
        "inputs": [
            {"name": "owner", "type": "address"},
            {"name": "spender", "type": "address"},
            {"name": "amount", "type": "uint256"},
            {"name": "expiry", "type": "uint256"},
            {"name": "signature", "type": "bytes"},
        ],
        "outputs": [{"name": "", "type": "bool"}],
        "gas": 81264,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "totalAssets",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 4098,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "deposit",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "deposit",
        "inputs": [{"name": "_amount", "type": "uint256"}],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "deposit",
        "inputs": [
            {"name": "_amount", "type": "uint256"},
            {"name": "recipient", "type": "address"},
        ],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "maxAvailableShares",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 383839,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "withdraw",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "withdraw",
        "inputs": [{"name": "maxShares", "type": "uint256"}],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "withdraw",
        "inputs": [
            {"name": "maxShares", "type": "uint256"},
            {"name": "recipient", "type": "address"},
        ],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "withdraw",
        "inputs": [
            {"name": "maxShares", "type": "uint256"},
            {"name": "recipient", "type": "address"},
            {"name": "maxLoss", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "pricePerShare",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 18195,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "addStrategy",
        "inputs": [
            {"name": "strategy", "type": "address"},
            {"name": "debtRatio", "type": "uint256"},
            {"name": "minDebtPerHarvest", "type": "uint256"},
            {"name": "maxDebtPerHarvest", "type": "uint256"},
            {"name": "performanceFee", "type": "uint256"},
        ],
        "outputs": [],
        "gas": 1485796,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "updateStrategyDebtRatio",
        "inputs": [
            {"name": "strategy", "type": "address"},
            {"name": "debtRatio", "type": "uint256"},
        ],
        "outputs": [],
        "gas": 115193,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "updateStrategyMinDebtPerHarvest",
        "inputs": [
            {"name": "strategy", "type": "address"},
            {"name": "minDebtPerHarvest", "type": "uint256"},
        ],
        "outputs": [],
        "gas": 42441,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "updateStrategyMaxDebtPerHarvest",
        "inputs": [
            {"name": "strategy", "type": "address"},
            {"name": "maxDebtPerHarvest", "type": "uint256"},
        ],
        "outputs": [],
        "gas": 42471,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "updateStrategyPerformanceFee",
        "inputs": [
            {"name": "strategy", "type": "address"},
            {"name": "performanceFee", "type": "uint256"},
        ],
        "outputs": [],
        "gas": 41251,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "migrateStrategy",
        "inputs": [
            {"name": "oldVersion", "type": "address"},
            {"name": "newVersion", "type": "address"},
        ],
        "outputs": [],
        "gas": 1141468,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "revokeStrategy",
        "inputs": [],
        "outputs": [],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "revokeStrategy",
        "inputs": [{"name": "strategy", "type": "address"}],
        "outputs": [],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "addStrategyToQueue",
        "inputs": [{"name": "strategy", "type": "address"}],
        "outputs": [],
        "gas": 1199804,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "removeStrategyFromQueue",
        "inputs": [{"name": "strategy", "type": "address"}],
        "outputs": [],
        "gas": 23088703,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "debtOutstanding",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "debtOutstanding",
        "inputs": [{"name": "strategy", "type": "address"}],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "creditAvailable",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "creditAvailable",
        "inputs": [{"name": "strategy", "type": "address"}],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "availableDepositLimit",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 9551,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "expectedReturn",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "expectedReturn",
        "inputs": [{"name": "strategy", "type": "address"}],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "report",
        "inputs": [
            {"name": "gain", "type": "uint256"},
            {"name": "loss", "type": "uint256"},
            {"name": "_debtPayment", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 1015170,
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "sweep",
        "inputs": [{"name": "token", "type": "address"}],
        "outputs": [],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "sweep",
        "inputs": [
            {"name": "token", "type": "address"},
            {"name": "amount", "type": "uint256"},
        ],
        "outputs": [],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "name",
        "inputs": [],
        "outputs": [{"name": "", "type": "string"}],
        "gas": 8750,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "symbol",
        "inputs": [],
        "outputs": [{"name": "", "type": "string"}],
        "gas": 7803,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "decimals",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2408,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "precisionFactor",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2438,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "balanceOf",
        "inputs": [{"name": "arg0", "type": "address"}],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2683,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "allowance",
        "inputs": [
            {"name": "arg0", "type": "address"},
            {"name": "arg1", "type": "address"},
        ],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2928,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "totalSupply",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2528,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "token",
        "inputs": [],
        "outputs": [{"name": "", "type": "address"}],
        "gas": 2558,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "governance",
        "inputs": [],
        "outputs": [{"name": "", "type": "address"}],
        "gas": 2588,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "management",
        "inputs": [],
        "outputs": [{"name": "", "type": "address"}],
        "gas": 2618,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "guardian",
        "inputs": [],
        "outputs": [{"name": "", "type": "address"}],
        "gas": 2648,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "guestList",
        "inputs": [],
        "outputs": [{"name": "", "type": "address"}],
        "gas": 2678,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "strategies",
        "inputs": [{"name": "arg0", "type": "address"}],
        "outputs": [
            {"name": "performanceFee", "type": "uint256"},
            {"name": "activation", "type": "uint256"},
            {"name": "debtRatio", "type": "uint256"},
            {"name": "minDebtPerHarvest", "type": "uint256"},
            {"name": "maxDebtPerHarvest", "type": "uint256"},
            {"name": "lastReport", "type": "uint256"},
            {"name": "totalDebt", "type": "uint256"},
            {"name": "totalGain", "type": "uint256"},
            {"name": "totalLoss", "type": "uint256"},
        ],
        "gas": 11031,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "withdrawalQueue",
        "inputs": [{"name": "arg0", "type": "uint256"}],
        "outputs": [{"name": "", "type": "address"}],
        "gas": 2847,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "emergencyShutdown",
        "inputs": [],
        "outputs": [{"name": "", "type": "bool"}],
        "gas": 2768,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "depositLimit",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2798,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "debtRatio",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2828,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "totalDebt",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2858,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "lastReport",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2888,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "activation",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2918,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "lockedProfit",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2948,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "lockedProfitDegration",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 2978,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "rewards",
        "inputs": [],
        "outputs": [{"name": "", "type": "address"}],
        "gas": 3008,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "managementFee",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 3038,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "performanceFee",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 3068,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "nonces",
        "inputs": [{"name": "arg0", "type": "address"}],
        "outputs": [{"name": "", "type": "uint256"}],
        "gas": 3313,
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "DOMAIN_SEPARATOR",
        "inputs": [],
        "outputs": [{"name": "", "type": "bytes32"}],
        "gas": 3128,
    },
]