python3

djanjo

https://blog.csdn.net/luckytanggu/article/details/53491892

pil实现截图     
python3用pillow     
微软的3389使用的RDP协议（远程桌面协议，Remote Desktop Protocol）
它仅传输服务器所显示的对象的属性变化的控制值，实现快速远程控制，相对于其它采用抓屏图片压缩的远程控制软件，速度更快，控制更准确。    
差异截图用的较多的是XOR，这样可以降低传输数据，你说的是分块差异传输     
基于消息机制的是hook各种窗口变化消息，然后合并各个变化矩形，找出最小变化矩  形，然后截取发送      
目前比较好的算法是隔行扫描，包括固定块隔行扫描，和分块隔行扫描等，redmin,黑洞，gh0st等都用的这个算法    
mirror驱动也是应用的比较多的一种，有兴趣的可以加QQ群63581069，大家讨论讨论  

RDP协议我在MSDN里看过了，它是用于处理数据传输部分的，我想知道的是截图原理。     
听你这么一说我也想起来了，确实见过有XOR整个图象，然后压缩传输的算法。由于相同部分异或后内容为0，所以压缩比较高。也许我看的那段代码很老，xor加分块的方法速度并没有多大提升，主要还是因为需要逐一比较分块是否改变，而且之前对全图xor还导致速度的下降。    

我想知道它们是如何确定需要重传的分块的，或者这个比较过程用了什么特殊的手法以加快处理速度？隔行扫描占用CPU确实很小，不过如果不判断哪些行需要重传，占用带宽还是很大的。结果又绕回如何确定是否需要重传上来了...    
我对驱动不太熟悉，而且感觉这么一个小东西搬个驱动过来，有点小题大做了（我不想写远控程序，也不用进程隐藏，只要能实现高速的屏幕传输就行了(主要是刷新频率要求较高，至少每秒5-10帧吧)）。看来还是要从分块隔行扫描入手。  
截屏算法        
http://www.dewen.net.cn/q/484/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%BF%AB%E9%80%9F%E5%B1%8F%E5%B9%95%E4%BC%A0%E9%80%81%E7%AE%97%E6%B3%95%EF%BC%9F     

