use std::str::FromStr;

static INPUT: &str = "input";

#[derive(Eq, PartialEq, Clone, Copy, Hash, Debug)]
#[repr(u8)]
enum OpCode {
    Addr,
    Addi,
    Mulr,
    Muli,
    Banr,
    Bani,
    Borr,
    Bori,
    Setr,
    Seti,
    Gtir,
    Gtri,
    Gtrr,
    Eqir,
    Eqri,
    Eqrr,
}

impl FromStr for OpCode {
    type Err = &'static str;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(match s {
            "addr" => OpCode::Addr,
            "addi" => OpCode::Addi,
            "mulr" => OpCode::Mulr,
            "muli" => OpCode::Muli,
            "banr" => OpCode::Banr,
            "bani" => OpCode::Bani,
            "borr" => OpCode::Borr,
            "bori" => OpCode::Bori,
            "setr" => OpCode::Setr,
            "seti" => OpCode::Seti,
            "gtir" => OpCode::Gtir,
            "gtri" => OpCode::Gtri,
            "gtrr" => OpCode::Gtrr,
            "eqir" => OpCode::Eqir,
            "eqri" => OpCode::Eqri,
            "eqrr" => OpCode::Eqrr,
            _ => panic!("invalid"),
        })
    }
}

#[derive(Eq, PartialEq, Clone, Copy, Hash, Debug)]
struct Op {
    code: OpCode,
    a: usize,
    b: usize,
    c: usize,
}

impl std::str::FromStr for Op {
    type Err = &'static str;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut it = s.split_whitespace();
        let code = it.next().unwrap().parse().unwrap();
        let a = it.next().unwrap().parse().unwrap();
        let b = it.next().unwrap().parse().unwrap();
        let c = it.next().unwrap().parse().unwrap();
        Ok(Op { code, a, b, c })
    }
}

struct Device {
    regs: [usize; 6],
    ip: usize,
    ops: Vec<Op>,
}

impl Device {
    fn raw_op(&mut self, op: OpCode, a: usize, b: usize, c: usize) {
        use self::OpCode::*;
        match op {
            Addr => self.regs[c] = self.regs[a] + self.regs[b],
            Addi => self.regs[c] = self.regs[a] + b,
            Mulr => self.regs[c] = self.regs[a] * self.regs[b],
            Muli => self.regs[c] = self.regs[a] * b,
            Banr => self.regs[c] = self.regs[a] & self.regs[b],
            Bani => self.regs[c] = self.regs[a] & b,
            Borr => self.regs[c] = self.regs[a] | self.regs[b],
            Bori => self.regs[c] = self.regs[a] | b,
            Setr => self.regs[c] = self.regs[a],
            Seti => self.regs[c] = a,
            Gtir => self.regs[c] = (a > self.regs[b]) as usize,
            Gtri => self.regs[c] = (self.regs[a] > b) as usize,
            Gtrr => self.regs[c] = (self.regs[a] > self.regs[b]) as usize,
            Eqir => self.regs[c] = (a == self.regs[b]) as usize,
            Eqri => self.regs[c] = (self.regs[a] == b) as usize,
            Eqrr => self.regs[c] = (self.regs[a] == self.regs[b]) as usize,
        }
    }

    fn op(&mut self) {
        println!("regs: {:?}", self.regs);
        let Op { code, a, b, c } = self.ops[self.regs[self.ip]];
        self.raw_op(code, a, b, c);
        self.regs[self.ip] += 1;
    }
}

fn main() {
    let mut input = aoc::file::to_strings_iter(INPUT);
    let ip = input.next().unwrap().trim_start_matches("#ip ").parse().unwrap();
    let ops = input
        .map(|v| {
            match v.parse() {
                Ok(vp) => vp,
                _ => panic!("parse error for input: {}", v),
            }
        })
        .collect();
    let mut dev = Device { regs: [0; 6], ip, ops };
    while dev.regs[dev.ip] < dev.ops.len() {
        dev.op();
    }
    println!("  1: {}", dev.regs[0]);
    // below is determined by examining the results of running the input for a little while
    let p2 = 10551364;
    println!("  2: {}", p2 + (1..=p2/2).filter(|x| p2 % x == 0).sum::<u32>());
}
