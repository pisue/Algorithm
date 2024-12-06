class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String[] posArr = pos.split(":");
        String[] videoLengArr = video_len.split(":");
        String[] opStartArr = op_start.split(":");
        String[] opEndArr = op_end.split(":");
        
        int posSec = calcMin(posArr[0], posArr[1]);
        int videoSec = calcMin(videoLengArr[0], videoLengArr[1]);
        int opStartSec = calcMin(opStartArr[0], opStartArr[1]);
        int opEndSec = calcMin(opEndArr[0], opEndArr[1]);
        if(opStartSec<=posSec && posSec <= opEndSec) {
            posSec = opEndSec;
        }
        
        for(String command : commands){
            posSec = calcCommand(posSec, command, videoSec);
            posSec = chkOp(opStartSec, opEndSec, posSec);
        }
        
        int resultMin = posSec/60;
        int resultSec = posSec%60;
        String answerMin = addZero(String.valueOf(resultMin));
        String answerSec = addZero(String.valueOf(resultSec));
        
        
        
        return answerMin + ":" + answerSec;
    }
    
    public int calcMin(String min, String sec){
        int minToSec = Integer.parseInt(min)*60;
    
        return minToSec + Integer.parseInt(sec);
    }
    
    public int calcCommand(int posSec, String command, int videoSec){
        int calcSec;
        if(command.equals("next")){
            calcSec = posSec+10;
            if(calcSec>videoSec){
                calcSec = videoSec;
            }
        }else{
            calcSec = posSec-10;
            if(calcSec<0){
                calcSec = 0;
            }
            
        }
        
        return calcSec;
    }
    
    public String addZero(String str){
        if(str.length() == 1){
            str = "0"+str;
        }
        
        return str;
    }
    
    public int chkOp(int opStartSec, int opEndSec, int posSec){
        if(opStartSec<=posSec && posSec <= opEndSec){
            posSec = opEndSec;
        }
        
        return posSec;
    }
}