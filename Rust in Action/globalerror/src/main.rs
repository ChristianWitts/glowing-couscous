//extern crate rand;
use rand::{thread_rng, Rng};

static mut ERROR: isize = 0;

struct File;

#[allow(unused_variables)]
fn read(f: &File, save_to: Vec<u8>) -> usize {
    // "read from disk"
    rng = thread_rng();
    if rng.gen_weighted_bool(10_000) {
        unsafe {
            ERROR = 1;
        }
    }

    0
}

#[allow(unused_mut)]
fn main() {
    let mut f = File;
    let mut buffer = vec![];

    read(&f, buffer);
    unsafe {
        if ERROR != 0 {
            panic!("an error has occured")
        }
    }
}

