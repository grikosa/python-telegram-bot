импортный  телебот

бот  =  телебот . TeleBot ( «1268739906:AAH3nyLDfCuVe9XLMD3o7HLd0kPyEbsHheI» )

@ бот . message_handler ( commands = [ 'start' , 'help' ]) 
def  send_welcome ( сообщение ):
	 бот . reply_to ( сообщение , "Привет, как дела?" )

@ бот . message_handler ( func = лямбда-  сообщение : True ) 
def  echo_all ( message ):
	 bot . reply_to ( сообщение , сообщение . текст )

бот . опрос ()
