class Gold{
  int w;
  int v;
  public Gold(int w, int v) {
    this.w = w;
    this.v = v;
  }
}

class Chromosome implements Comparable<Chromosome>, Cloneable{
  int sum = 0;
  int val = 0;
  int[] code;
  @Override
  public int compareTo(Chromosome o) {
    return o.val - this.val;
  }
  public void setSumVal() {
    this.sum = 0;
    this.val = 0;
    for(int i = 0; i < code.length ; i++) {
      if(code[i] == 1) {
        this.sum += golds[i].w;
        this.val += golds[i].v;
      }
    }
  }
  //깊은 복사를 위한 메소드
  public Chromosome clone() {
    Chromosome ch = null;
    try {
      ch = (Chromosome) super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return ch;		
  }

}