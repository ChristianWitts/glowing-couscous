extern crate itertools;
extern crate linked_hash_set;
use itertools::Itertools;
use std::collections::HashMap;
use std::collections::HashSet;
use linked_hash_set::LinkedHashSet;


#[derive(Debug, Copy, Clone)]
enum OpType {
    add,
    set,
    mul,
    ban,
    bor,
    gt,
    eq
}

#[derive(Debug, Copy, Clone)]
enum Mode {
    Value,
    Register
}

#[derive(Debug, Copy, Clone)]
struct Instruction {
    op: OpType,
    mode_a: Mode,
    mode_b: Mode,
    a: i64,
    b: i64,
    c: i64
}

#[derive(Debug)]
struct Program {
    ip_register: usize,
    instructions: Vec<Instruction>
}

fn resolve(registers: &[i64], mode: Mode, value: i64) -> i64 {
    match mode {
        Mode::Value => value,
        Mode::Register => registers[value as usize]
    }
}

impl Program {
    fn execute(&self) -> LinkedHashSet<i64> {
        let mut values = LinkedHashSet::new();
        let mut registers = vec![0i64; 6];


        let mut ip = 0;
        loop {
            registers[self.ip_register] = ip;

            if ip as usize >= self.instructions.len() {
                break;
            }
            let instruction = self.instructions[ip as usize];

            if ip == 28 {
                if values.contains(&registers[4]) {
                    break;
                }
                values.insert(registers[4]);
            }
            if ip > 25 {
                continue;
                // println!("{} {:?}", ip, registers);
            }

            let value_a = resolve(&registers, instruction.mode_a, instruction.a);
            let value_b = resolve(&registers, instruction.mode_b, instruction.b);

            let result = match instruction.op {
                OpType::add => value_a + value_b,
                OpType::mul => value_a * value_b,
                OpType::ban => value_a & value_b,
                OpType::bor => value_a | value_b,
                OpType::gt => (value_a > value_b) as i64,
                OpType::eq => (value_a == value_b) as i64,
                OpType::set => value_a
            };

            registers[instruction.c as usize] = result;

            ip = registers[self.ip_register];
            ip += 1;

        }
        values
    }
}

fn parse_op(op: &str) -> (OpType, Mode, Mode) {
    match op {
        "addr" => (OpType::add, Mode::Register, Mode::Register),
        "addi" => (OpType::add, Mode::Register, Mode::Value),
        "mulr" => (OpType::mul, Mode::Register, Mode::Register),
        "muli" => (OpType::mul, Mode::Register, Mode::Value),
        "banr" => (OpType::ban, Mode::Register, Mode::Register),
        "bani" => (OpType::ban, Mode::Register, Mode::Value),
        "borr" => (OpType::bor, Mode::Register, Mode::Register),
        "bori" => (OpType::bor, Mode::Register, Mode::Value),
        "setr" => (OpType::set, Mode::Register, Mode::Value),
        "seti" => (OpType::set, Mode::Value, Mode::Value),
        "gtir" => (OpType::gt, Mode::Value, Mode::Register),
        "gtri" => (OpType::gt, Mode::Register, Mode::Value),
        "gtrr" => (OpType::gt, Mode::Register, Mode::Register),
        "eqir" => (OpType::eq, Mode::Value, Mode::Register),
        "eqri" => (OpType::eq, Mode::Register, Mode::Value),
        "eqrr" => (OpType::eq, Mode::Register, Mode::Register),
        _ => panic!("{}", op)
    }
}

fn parse(text: &str) -> Program {
    let mut lines = text.lines();

    let ip_line = lines.next().unwrap();
    assert!(ip_line.starts_with("#ip"));
    let ip_register: usize = ip_line.split_whitespace().collect_vec()[1].parse().unwrap();

    let instructions = lines.map(|line| {
        let parts = line.split_whitespace().collect_vec();
        let (op, mode_a, mode_b) = parse_op(parts[0]);
        Instruction {
            op,mode_a,mode_b, a: parts[1].parse().unwrap(),
            b: parts[2].parse().unwrap(),
            c: parts[3].parse().unwrap()
        }
    }).collect();

    Program {ip_register,instructions}
}

fn main() {
    let text = include_str!("input");
    let program = parse(text);
    let mut values = program.execute();
    println!("Part 1: {}", values.front().unwrap());
    println!("Part 2: {}", values.back().unwrap());
}
