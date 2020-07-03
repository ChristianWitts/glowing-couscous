#include <iostream>
#include <vector>
#include <cstring>
#include <set>

using namespace std;
struct instruct{
  string op;
  long long a, b, c;
};

string s;

int ip;

vector<instruct> v;

set<long long> pos;
long long last;

long long reg[6];

int uintaj(string s){
  int z = (s[0] - '0');
  for (int i = 1; i < (int) s.size(); i++){
    z *= 10;
    z += (s[i] - '0');
  }
  return z;
}

int main (void){
  while (getline(cin, s)){
    if (s[0] == '#'){
      ip = uintaj(s.substr(4));
    }
    else{
      instruct tmp;
      tmp.op = s.substr(0, 4);
      s = s.substr(5);

      int i;
      for (i = 0; s[i] != ' '; i++);
      tmp.a = uintaj(s.substr(0, i));
      s = s.substr(i + 1);

      for (i = 0; s[i] != ' '; i++);
      tmp.b = uintaj(s.substr(0, i));
      tmp.c = uintaj(s.substr(i + 1));

      v.push_back(tmp);
    }
  }

  for (;reg[ip] < (int) v.size(); reg[ip]++){
    if (reg[ip] == 28){
      if (pos.find(reg[3]) != pos.end()){
        cout << last << endl;
        break;
      }

      last = reg[3];
      pos.insert(reg[3]);
    }
    if (v[reg[ip]].op == "addi"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] + v[reg[ip]].b);
    }
    else if (v[reg[ip]].op == "addr"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] + reg[v[reg[ip]].b]);
    }
    else if (v[reg[ip]].op == "muli"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] * v[reg[ip]].b);
    }
    else if (v[reg[ip]].op == "mulr"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] * reg[v[reg[ip]].b]);
    }
    else if (v[reg[ip]].op == "bani"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] & v[reg[ip]].b);
    }
    else if (v[reg[ip]].op == "banr"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] & reg[v[reg[ip]].b]);
    }
    else if (v[reg[ip]].op == "bori"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] | v[reg[ip]].b);
    }
    else if (v[reg[ip]].op == "borr"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] | reg[v[reg[ip]].b]);
    }
    else if (v[reg[ip]].op == "seti"){
      reg[v[reg[ip]].c] = v[reg[ip]].a;
    }
    else if (v[reg[ip]].op == "setr"){
      reg[v[reg[ip]].c] = reg[v[reg[ip]].a];
    }
    else if (v[reg[ip]].op == "gtri"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] > v[reg[ip]].b);
    }
    else if (v[reg[ip]].op == "gtir"){
      reg[v[reg[ip]].c] = (v[reg[ip]].a > reg[v[reg[ip]].b]);
    }
    else if (v[reg[ip]].op == "gtrr"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] > reg[v[reg[ip]].b]);
    }
    else if (v[reg[ip]].op == "eqri"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] == v[reg[ip]].b);
    }
    else if (v[reg[ip]].op == "eqir"){
      reg[v[reg[ip]].c] = (v[reg[ip]].a == reg[v[reg[ip]].b]);
    }
    else if (v[reg[ip]].op == "eqrr"){
      reg[v[reg[ip]].c] = (reg[v[reg[ip]].a] == reg[v[reg[ip]].b]);
    }
  }

  return 0;
}
