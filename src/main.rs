use std::{fs::File, io::Read};

fn main() {
    println!("Hello, world!");

    let path = "D:\\Skyrim Se alll\\Mod Organizer 2\\Mods\\[Melodic] Mauree outfit SE 3BA\\[Melodic] Mauree outfit SE 3BA.esp";

    let mut file_content =  Vec:: new();
    let mut file = File::open(path).expect("could not read");

    file.read_to_end(&mut file_content).expect("cannot read fiel content");


    const GRUP: &str = "GRUP";
    const GRUP_VEC: &[u8] = GRUP.as_bytes();


    match file_content.windows(GRUP_VEC.len()).find(|&window| window == GRUP_VEC){
        Some(res) => println!("{:?}",res),
        None => println!("Pattern not found using pattern matching"),
    }

    for chunk in file_content.chunks(4){
        //println!("{:?} = {:?}",grup_vec,chunk);
        if(chunk.eq(GRUP_VEC)){
            let memloc= chunk.as_ptr();
            //print!("{:?}",chunk[3]);
            
            let lastmemloc = memloc.wrapping_add(std::mem::size_of::<u8>()*4 );//+std::mem::size_of::<u32>()
            println!("{:?}",lastmemloc);
            
        }
    }

    
}
fn u32_to_vecu8(s:u32)->Vec<u8> {
    
    let mut out:Vec<u8> = Vec::new();

    out.push( ((s >> 24) & 0xFF) as u8);
    out.push( ((s >> 16) & 0xFF) as u8);
    out.push( ((s >> 8) & 0xFF) as u8);
    out.push( (s & 0xFF) as u8);

    out
}