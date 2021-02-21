struct IntCodeComputer {
    memory: Vec<u32>,
    pointer: usize,
}

struct Operation {
    opcode: u32,
    rAdd1: MemAddress,
    rAdd2: MemAddress,
    wAdd: MemAddress
}

struct MemAddress {
    index: usize,
    mode: AddressMode
}

enum AddressMode {
    direct,
    indirekt
}

impl IntCodeComputer {
    fn new() -> IntCodeComputer {
        IntCodeComputer {
            memory: Vec::new(),
            pointer: 0
        }
    }

    fn run(&mut self){
        
    }

    fn execute(&mut self, operation: Operation) -> u32{
        match operation.opcode {
            0 => {
                let pointer = self.get_mut(operation.wAdd);
                pointer = self.get(operation.rAdd1) + self.get(operation.rAdd2);
                4
            }
        }

    }

    fn add(&mut self, address: MemAddress){

    }

    fn get_mut(&mut self, addr: MemAddress) -> &mut u32 {
        match addr.mode {
            AddressMode::direct => {
                let pointer:&mut u32 = self.memory[addr.index];
            }
            AddressMode::indirekt => {

            }
        }
        
    }

    fn get(&self, address: MemAddress) -> u32 {
        return 42
    }
}



#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}

