package py4j;
public class PingPlayer 
{
    public int multi(int a)
    {
        return a*100;
    }

    public int multi2(int a)
    
    {
        return a*200;
    }
    public int divi(int a)
    {
        return a/2;
    }
    public void resp(PongPlayer a)
    {
        String st= a.response2();
        System.out.println(st);
    }
    public void sum(PongPlayer a)
    {
        int x=a.plus(45, 66);
        System.out.println(x);
    }
     public static void main(String[] args) {
        PingPlayer y=new PingPlayer();
        GatewayServer gatewayServer = new GatewayServer(y);
        gatewayServer.start();
        System.out.println("Gateway Server Started");
        // int summ=player.plus(12,45);
        // System.out.println(summ);
}}