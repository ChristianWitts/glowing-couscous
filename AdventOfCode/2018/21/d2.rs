use std::io::{self, BufRead};
use std::collections::HashSet;

#[derive(Copy, Clone, Debug)]
struct Registers {
    ip: usize,
    registers: [usize; 6],
}

impl Registers {
    fn new() -> Registers {
        Registers {
            ip: 0,
            registers: [0; 6],
        }
    }

    fn set_ip(&mut self, s: &str) {
        self.ip = s.split_whitespace().nth(1).unwrap().parse().unwrap()
    }
}

#[derive(Clone, Debug)]
struct Instruction {
    opcode: String,
    a: usize,
    b: usize,
    c: usize,
}

impl Instruction {
    fn new(s: &str) -> Instruction {
        let mut iter = s.split_whitespace();

        Instruction {
            opcode: iter.next().unwrap().into(),
            a: iter.next().unwrap().parse().unwrap(),
            b: iter.next().unwrap().parse().unwrap(),
            c: iter.next().unwrap().parse().unwrap(),
        }
    }
}

fn execute(inst: &Instruction, regs: &mut Registers) {
    let reg = &mut regs.registers;

    match inst.opcode.as_str() {
    "addr" => reg[inst.c] = reg[inst.a] + reg[inst.b],
    "addi" => reg[inst.c] = reg[inst.a] + inst.b,
    "mulr" => reg[inst.c] = reg[inst.a] * reg[inst.b],
    "muli" => reg[inst.c] = reg[inst.a] * inst.b,
    "banr" => reg[inst.c] = reg[inst.a] & reg[inst.b],
    "bani" => reg[inst.c] = reg[inst.a] & inst.b,
    "borr" => reg[inst.c] = reg[inst.a] | reg[inst.b],
    "bori" => reg[inst.c] = reg[inst.a] | inst.b,
    "setr" => reg[inst.c] = reg[inst.a],
    "seti" => reg[inst.c] = inst.a,
    "gtir" => reg[inst.c] = (inst.a > reg[inst.b]) as usize,
    "gtri" => reg[inst.c] = (reg[inst.a] > inst.b) as usize,
    "gtrr" => reg[inst.c] = (reg[inst.a] > reg[inst.b]) as usize,
    "eqir" => reg[inst.c] = (inst.a == reg[inst.b]) as usize,
    "eqri" => reg[inst.c] = (reg[inst.a] == inst.b) as usize,
    "eqrr" => reg[inst.c] = (reg[inst.a] == reg[inst.b]) as usize,
    _ => panic!("unkown instruction {}", inst.opcode.as_str()),
    }
}

fn main() {
    let stdin = io::stdin();
    let mut reg = Registers::new();
    let mut insts = Vec::new();
    let mut ip = 0;

    for line in stdin.lock().lines().map(|x| x.unwrap()) {
        if line.starts_with("#") {
            reg.set_ip(&line);
        } else {
            insts.push(Instruction::new(&line));
        }
    }

    while ip < insts.len() {
        reg.registers[reg.ip] = ip;
        execute(&insts[reg.registers[reg.ip]], &mut reg);
        ip = reg.registers[reg.ip] + 1;

        if reg.registers[reg.ip] == 28 {
            break;
        }
    }

    println!("{}", reg.registers[3]);
}

// fn main() {
//     let stdin = io::stdin();
//     let mut reg = Registers::new();
//     let mut insts = Vec::new();
//     let mut ip = 0;
//     let mut seen = HashSet::new();
//     let mut last = 0;

//     for line in stdin.lock().lines().map(|x| x.unwrap()) {
//         if line.starts_with("#") {
//             reg.set_ip(&line);
//         } else {
//             insts.push(Instruction::new(&line));
//         }
//     }

//     while ip < insts.len() {
//         reg.registers[reg.ip] = ip;
//         execute(&insts[reg.registers[reg.ip]], &mut reg);
//         ip = reg.registers[reg.ip] + 1;

//         if reg.registers[reg.ip] == 28 {
//             if seen.get(&reg.registers[3]).is_some() {
//                 break;
//             }

//             seen.insert(reg.registers[3]);
//             last = reg.registers[3];
//         }
//     }

//     println!("{}", last);
// }

// #ip 2
// 00 seti 123     0       3 // reg[3] = 123
// 01 bani 3       456     3 // reg[3] |= 456
// 02 eqri 3       72      3 // reg[3] == 72 { goto 5 } else { goto 4 }
// 03 addr 3       2       2
// 04 seti 0       0       2 // goto 1
// 05 seti 0       0       3 // reg[3] = 0
// 06 bori 3       65536       4 // reg[4] = reg[3] | 65536
// 07 seti 10649702    3       3 // reg[3] = 10649702
// 08 bani 4       255     5 // reg[5] = reg[4] & 255
// 09 addr 3       5       3 // reg[3] += reg[5]
// 10 bani 3       16777215    3 // reg[3] &= 16777215
// 11 muli 3       65899       3 // reg[3] *= 65899
// 12 bani 3       16777215    3 // reg[3] &= 16777215
// 13 gtir 256     4       5 // if 256 > reg[4] { goto 16 } else { goto 15}
// 14 addr 5       2       2
// 15 addi 2       1       2 // goto 17
// 16 seti 27      7       2 // goto 28
// 17 seti 0       6       5 // reg[5] = 0
// 18 addi 5       1       1 // reg[1] = reg[5] + 1
// 19 muli 1       256     1 // reg[1] *= 256
// 20 gtrr 1       4       1 // if reg[1] > reg[4] { goto 23 } else { goto 22 }
// 21 addr 1       2       2
// 22 addi 2       1       2 // goto 24
// 23 seti 25      9       2 // goto 26
// 24 addi 5       1       5 // reg[5] += 1
// 25 seti 17      9       2 // goto 18
// 26 setr 5       7       4 // reg[4] = reg[5]
// 27 seti 7       1       2 // goto 8
// 28 eqrr 3       0       5 // if reg[3] == reg[0] { halt } else { goto 6 }
// 29 addr 5       2       2
// 30 seti 5       4       2
