
from solcx import compile_standard
import json 
with open("./SIMPLsTORAGE.SOL", "r") as file:
    simple_storage_file = file.read()
    compiled_sol=compile_standard(
        {
            "language":"Solidity",
            "sources":{"SIMPLsTORAGE.SOL":{"content":simple_storage_file}},
            "settinigs":{
                "outputSelection":{
                    "*":{
                        "*":["abi","metadata","evm.bytecode","evm.sourceMap"]
                    }
                }
            },

        },
        solc_version="0.8.0",
    )
    with open("compiled+code.json","w") as file:
        json.dump(compiled_sol,file)
  
bytecode = compiled_sol["contracts"]["simplestorage.sol"]["simplestorage"]["evm"]
[
    "bytecode"
]["object"]


