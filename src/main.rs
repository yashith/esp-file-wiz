use std::{fs::File, io::Read, f32::consts::E, ops::Add};

fn main() {
    println!("Hello, world!");

    let path = "D:\\Skyrim Se alll\\Mod Organizer 2\\Mods\\[Melodic] Mauree outfit SE 3BA\\[Melodic] Mauree outfit SE 3BA.esp";

    let mut file_content =  Vec:: new();
    let mut file = File::open(path).expect("could not read");

    file.read_to_end(&mut file_content).expect("cannot read fiel content");


    println!("{:?}",check_tes(&file_content));
    if check_tes(&file_content){
    let li = find_groups(&file_content);
    print!("{:?}",li);

    }
}
fn check_tes(fc:&Vec<u8>) -> bool{
   let testv ="TES4";
   let tesv_v = testv.as_bytes();
   //[..4] take next 4 locations from fc 
   return fc[..4] ==*tesv_v;  
}
fn find_groups(fc:&Vec<u8>)->Vec<*const u8>{
    let g = "GRUP";
    let mut out = Vec::new();
    for window in fc.windows(4){
        if window==g.as_bytes(){
            out.push(window.as_ptr());
        }

    }
return out; 
}
fn get_group_size(gr_begining:*const u8)->u32{
    let size:u32 =0; 
    return size;
}