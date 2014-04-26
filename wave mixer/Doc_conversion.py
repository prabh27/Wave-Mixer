#!/usr/bin/python
# -*- coding: utf-8 -*-
# example buttonbox.py



import pygtk
pygtk.require('2.0')
import gtk
import os
import re
import subprocess
from bs4 import BeautifulSoup
import sys
from subprocess import call


def xpm_label_box(parent, xpm_filename, label_text):
	# Create box for xpm and label
	box1 = gtk.HBox(False, 0)
	box1.set_border_width(2)
	# Now on to the image stuff
	image = gtk.Image()
	image.set_from_file(xpm_filename)
	# Create a label for the button
	label = gtk.Label(label_text)
	# Pack the pixmap and label into the box
	box1.pack_start(image, False, False, 3)
	box1.pack_start(label, False, False, 3)
	image.show()
	label.show()
	return box1
class ButtonBoxExample:
	def page_1(self):
		self.ou=0
		self.label123=-1
		self.label123=-1
		self.script="1st"
		self.script12="3rd"
		self.entry1234=-1
		self.world=-1
		self.file1=-1
		self.file21=-1
		self.final="English"
		self.file2=-1
		self.file5=-1
		self.file6=-1
		self.file7=-1
		self.ou=0
		self.entry1=-1
		self.entry=-1
		self.entry2=-1
		self.entry5=-1
		self.entry7=-1
		self.entry7=-1
		self.main_vbox1 = gtk.VBox(False, 0)
		self.window.add(self.main_vbox1)
		frame_vert = gtk.Frame()
		self.main_vbox1.pack_start(frame_vert, True, True, 10)
		hbox = gtk.HBox(False, 0)
		hbox.set_border_width(10)
		frame_vert.add(hbox)
		self.helloflag=0
		self.helloflag1=0
		hbox.pack_start(self.create_bbox1(True, "Selection",
			5, gtk.BUTTONBOX_START),
			True, True, 0)
		frame_horz = gtk.Frame()
		self.main_vbox1.pack_start(frame_horz, True, True, 10)
		vbox = gtk.HBox(False, 0)
		vbox.set_border_width(10)
		frame_horz.add(vbox)
		vbox.pack_start(self.create_bbox1(False, "        ",5, gtk.BUTTONBOX_END),True, True, 0)
		self.window.show_all()
	def create_bbox1(self, horizontal, title, spacing, layout):
		frame = gtk.Frame(title)
		if horizontal:
			self.bbox = gtk.VButtonBox()
			self.bbox.set_border_width(10)
			frame.add(self.bbox)
			print self.helloflag
			if self.helloflag==0 :
				button = gtk.RadioButton(None, "Document Conversion Tool")
				button.set_active(True)
				button.connect("toggled", self.callback1, "1st")
				self.bbox.pack_start(button, True, True, 0)
				button.show()
				button = gtk.RadioButton(button, "Alignment")
				button.connect("toggled", self.callback1, "2nd")
				button.show()
				self.bbox.pack_start(button, True, True, 0)
			else :
				print "asdffasdafsd"
				button = gtk.RadioButton(None, "Use Font Coverter")
				button.connect("toggled", self.callback12, "1st")
				self.bbox.pack_start(button, True, True, 0)
				button.show()
				button = gtk.RadioButton(button, "Use Mapping Script")
				button.connect("toggled", self.callback12, "2nd")
				self.bbox.pack_start(button, True, True, 0)
				button.show()
				button = gtk.RadioButton(button, "Plain Text File without above scripts")
				button.set_active(True)
				button.connect("toggled", self.callback12, "3rd")
				self.bbox.pack_start(button, True, True, 0)
				button.show()
			self.bbox.set_layout(layout)
			self.bbox.set_spacing(spacing)

		else:
			bbox = gtk.HButtonBox()
			bbox.set_border_width(10)
			frame.add(bbox)
			bbox.set_layout(layout)
			bbox.set_spacing(spacing)
			vbox = gtk.HButtonBox()
			vbox.set_layout(layout)
			vbox.set_border_width(1)
			button = gtk.Button(stock="Submit")
			map = button.get_colormap()
	 		color = map.alloc_color("light green")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)
			if self.helloflag1==0 :
				button.connect_object("clicked", self.submit_application1, self.window,None)
			else :
				button.connect_object("clicked", self.submit_application12, self.window,None)
			button.set_tooltip_text("Submit")
			vbox.add(button)
			if self.helloflag1==0 :
				button = gtk.Button(stock="Close")
				map = button.get_colormap()
	 			color = map.alloc_color("gray")
				style = button.get_style().copy()
	 			style.bg[gtk.STATE_NORMAL] = color
	    			button.set_style(style)
				button.connect_object("clicked", self.close_application, self.window,None)
				button.set_tooltip_text("Close the application")
				vbox.add(button)
			else :
				button = gtk.Button(stock="Back")
				map = button.get_colormap()
	 			color = map.alloc_color("gray")
				style = button.get_style().copy()
	 			style.bg[gtk.STATE_NORMAL] = color
	    			button.set_style(style)
				button.connect_object("clicked", self.Back_application12, self.window,None)
				button.set_tooltip_text("Back To Document Conversion Tool")
				vbox.add(button)
			bbox.add(vbox)
		return frame
	def callback1(self, widget, data=None):
		if(("ON")[widget.get_active()]):
			self.script=data;
	def callback12(self, widget, data=None):
		if(("ON")[widget.get_active()]):
			self.script12=data;
	def submit_application1(self, widget, event, data=None):
		if cmp(self.script,"1st")==0:
			self.window.remove(self.main_vbox1)
		#	self.window.add(self.main_vbox1)
			self.Document()
		if cmp(self.script,"2nd")==0:
			self.window.remove(self.main_vbox1)
			self.page_2()
	def submit_application12(self, widget, event, data=None):
		self.window.remove(self.main_vbox1)
		if cmp(self.script12,"2nd")==0:
			self.func1()
		else :
			self.hello()
	def submit_application3(self, widget, event, data=None):
		if self.file5 == -1 or self.file6 == -1 :
			self.window.remove(self.main_vbox)
			print "Oh Shit"
		else :
			#self.window.destroy()
			print "Got it"
			print self.file5
			print self.file6
			print self.file7
			self.align()
	def Document(self):
		self.label123=-1
		self.script="1st"
		self.world=-1
		self.file1=-1
		self.final="English"
		self.file2=-1
		self.entry1234=-1
		self.file5=-1
		self.file6=-1
		self.file7=-1
		self.file21=-1
		self.ou=0
		self.entry1=-1
		self.entry=-1
		self.entry2=-1
		self.script12="3rd"
		self.entry5=-1
		self.entry7=-1
		self.entry7=-1
		self.main_vbox = gtk.VBox(False, 0)
		self.window.add(self.main_vbox)
		frame_vert = gtk.Frame()
		self.main_vbox.pack_start(frame_vert, True, True, 10)
		hbox = gtk.HBox(False, 0)
		hbox.set_border_width(10)
		frame_vert.add(hbox)
		hbox.pack_start(self.create_bbox(True, "Language Selection",
			5, gtk.BUTTONBOX_EDGE),
			True, True, 0)
		frame_horz = gtk.Frame()
		self.main_vbox.pack_start(frame_horz, True, True, 10)
		vbox = gtk.HBox(False, 0)
		vbox.set_border_width(10)
		frame_horz.add(vbox)
		vbox.pack_start(self.create_bbox(False, "",5, gtk.BUTTONBOX_END),True, True, 0)
		self.window.show_all()
	def page_2(self):
		self.entry1234=-1
		self.main_vbox = gtk.VBox(False, 0)
		self.label123=-1
		self.script="1st"
		self.world=-1
		self.file1=-1
		self.final="English"
		self.file2=-1
		self.file5=-1
		self.file6=-1
		self.file7=-1
		self.ou=0
		self.file21=-1
		self.entry1=-1
		self.entry=-1
		self.script12="3rd"
		self.entry2=-1
		self.entry5=-1
		self.entry7=-1
		self.entry7=-1
		self.my_flag=0
		self.window.add(self.main_vbox)
		frame_vert = gtk.Frame()
		self.main_vbox.pack_start(frame_vert, True, True, 10)
		hbox = gtk.HBox(False, 0)
		hbox.set_border_width(10)
		frame_vert.add(hbox)
		hbox.pack_start(self.create_bbox3(True, "",5, gtk.BUTTONBOX_END),True, True, 0)
		frame_horz = gtk.Frame()
		self.main_vbox.pack_start(frame_horz, True, True, 10)
		vbox = gtk.HBox(False, 0)
		vbox.set_border_width(10)
		frame_horz.add(vbox)
		vbox.pack_start(self.create_bbox3(False, "",5, gtk.BUTTONBOX_END),True, True, 0)
		self.window.show_all()
	def file_back(self, widget, data=None):
		dialog = gtk.FileChooserDialog("Open..",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("Images")
		filter.add_mime_type("image/png")
		filter.add_mime_type("image/jpeg")
		filter.add_mime_type("image/gif")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		filter.add_pattern("*.gif")
		filter.add_pattern("*.tif")
		filter.add_pattern("*.xpm")
		dialog.add_filter(filter)
		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			print dialog.get_filename(), 'selected'
			self.file1=dialog.get_filename()
			self.entry.insert_text(self.file1)
		elif response == gtk.RESPONSE_CANCEL:
			print 'Closed, no files selected'
		print self.file1
		dialog.destroy()
	def file_back3(self, widget, data):
		dialog = gtk.FileChooserDialog("Open..",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("Images")
		filter.add_mime_type("image/png")
		filter.add_mime_type("image/jpeg")
		filter.add_mime_type("image/gif")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		filter.add_pattern("*.gif")
		filter.add_pattern("*.tif")
		filter.add_pattern("*.xpm")
		dialog.add_filter(filter)
		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			if cmp(data,"English")==0 :
				self.file5=dialog.get_filename()
				self.entry5.insert_text(self.file5)
			if cmp(data,"Hindi")==0 :
				self.file6=dialog.get_filename()
				self.entry6.insert_text(self.file6)
			if cmp(data,"dict")==0 :
				self.file7=dialog.get_filename()
				self.entry7.insert_text(self.file7)
		elif response == gtk.RESPONSE_CANCEL:
			print 'Closed, no files selected'
		dialog.destroy()
	def file_back1(self, widget, data=None):
		dialog = gtk.FileChooserDialog("Open..",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("Images")
		filter.add_mime_type("image/png")
		filter.add_mime_type("image/jpeg")
		filter.add_mime_type("image/gif")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		filter.add_pattern("*.gif")
		filter.add_pattern("*.tif")
		filter.add_pattern("*.xpm")
		dialog.add_filter(filter)
		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			print dialog.get_filename(), 'selected'
			self.file2=dialog.get_filename()
			self.entry1.insert_text(self.file2)
		elif response == gtk.RESPONSE_CANCEL:
			print 'Closed, no files selected'
		print self.file1
		dialog.destroy()
	def file_back123(self, widget, data=None):
		dialog = gtk.FileChooserDialog("Open..",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)
		filter = gtk.FileFilter()
		filter.set_name("Images")
		filter.add_mime_type("image/png")
		filter.add_mime_type("image/jpeg")
		filter.add_mime_type("image/gif")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		filter.add_pattern("*.gif")
		filter.add_pattern("*.tif")
		filter.add_pattern("*.xpm")
		dialog.add_filter(filter)
		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			print dialog.get_filename(), 'selected'
			self.file21=dialog.get_filename()
			self.entry1234.insert_text(self.file21)
		elif response == gtk.RESPONSE_CANCEL:
			print 'Closed, no files selected'
		print self.file21
		dialog.destroy()
	def close_application(self, widget, event, data=None):
		gtk.main_quit()
		return False
	def call_back(self,combobox):
		if(1):
			model = combobox.get_model()
			index = combobox.get_active()
			self.final=model[index][0];
			#if cmp(self.final,"English")!=0:
			if 0 :
				print self.final
				if self.label123==-1 :
					self.label123=gtk.Label("Insert executable character Mapping Script file \nand appropriate interpreter should be written on the file")
					self.obs_box.add(self.label123)
				if self.world!=-1 :
					self.file2=-1
					self.obs_box.remove(self.world)
					self.world=-1
				self.world = gtk.HButtonBox()
				self.world.set_layout(gtk.BUTTONBOX_END)
				self.world.set_border_width(1)
				button = gtk.Button()
				map = button.get_colormap()
	 			color = map.alloc_color("light blue")
				style = button.get_style().copy()
	 			style.bg[gtk.STATE_NORMAL] = color
	    			button.set_style(style)
				self.entry1=gtk.Entry(max=0)
				self.entry1.set_editable(False)
				self.entry1.show()
				self.world.pack_start(self.entry1,True,True,0)
				box3 = xpm_label_box(self.window, "info.xpm", "Select the Script file")
				button.connect_object("clicked", self.file_back1,None)
				button.set_tooltip_text("Press this button to browse the file")
				self.world.add(button)
				button.add(box3)
				box3.show()
				button.show()
				self.world.show()
				self.obs_box.add(self.world)
				self.obs_box.show()
				self.window.show_all()
			#if cmp(self.final,"English")==0:
			if 1 :
				if self.world!=-1 :
					self.file2=-1
					self.obs_box.remove(self.world)
					self.obs_box.remove(self.label123)
					self.world=-1
					self.label123=-1
	def align(self):
                print os.getcwd()
                os.chdir("champollion11")
                pwd=os.getcwd()
                os.environ['CTK']=pwd
                #a="export CTK=`pwd`"
                #myname="export CTK=`pwd`"
                #os.system(a)
                os.chdir("./experiments/exp6_viv")
		if self.file7 !=-1 :
            	    subprocess.call(['../../bin/champollion','-d',self.file7, '-s','Function_words.en','-c','0.10',self.file5,self.file6,'EH1'],env=os.environ)
	    	else :
            	    subprocess.call(['../../bin/champollion','-d', "UW-English-Hindi.txt", '-s','Function_words.en','-c','0.10',self.file5,self.file6,'EH1'],env=os.environ)
                print os.getcwd()
                #myname="../../bin/champollion -d self.file7 -s Function_words.en -c 0.10 self.file5 self.file6 EH1"
                #os.system(myname)
		print "Your Text"
		dialog = gtk.FileChooserDialog("Save",None,gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
				#gtk.file_chooser.set_do_overwrite_confirmation (GTK_FILE_CHOOSER (dialog), TRUE);
				#dialog.set_current_name(text_file)
		response = dialog.run()
		if response == gtk.RESPONSE_OK:
				filename=dialog.get_filename()
				print filename
				#trew="mv ./champollion11/experiments/exp6_viv/EH1 "+filename
				trew="cp EH1 "+filename
				os.system(trew)
				#orig_stdout = sys.stdout;
				#sys.stdout = f;
		elif response == gtk.RESPONSE_CANCEL:
				print 'Closed, no files selected'
	#	sys.stdout = orig_stdout
		os.chdir("../../..")
		print os.getcwd()
		dialog.destroy()
		self.window.remove(self.main_vbox)
		self.page_1()
	def hello(self):
		print self.file1
		print self.final
		print self.file2
		new=-1
                if(re.search('.+\.html',self.file1)):
                    text_file = self.file1.replace('.html','.txt');
                elif(re.search('.+\.htm',self.file1)):
                    text_file = self.file1.replace('.htm','.txt');

		if(re.search('.+\.html',self.file1) or re.search('.+\.htm',self.file1)):
				#text_file = self.file1.replace('.html','.txt');
				if(os.path.isfile(text_file)):
						os.remove(text_file);
				if cmp(self.final,"English")==0:
				        my_name="python Extract_html.py "+self.file1+" "+text_file+" "+self.final
				        os.system(my_name)
					f = open(text_file,'r');
					old = f.read();
					f.close();
					new = old.split('\n');
					new = " ".join(new);
					new=re.sub('(?<!www)(?<![\s\n][0-9])\.(?!com)',".\n",new)
					new = re.sub('\?',"?\n",new);
					new = re.sub('!',"!\n",new);
                                        new=new.replace("\n.\n","\n");
                                        new=new.replace("\n.\n","\n");
                                        new=new.replace("\n.\n","\n");
                                        new=new.replace("\n.\n","\n");
                                        new=new.replace("\n.\n","\n");
                                        l=new.split("\n",1)
                                        if l[0]==".":
                                          new = l[1]
				elif cmp(self.final,"English")!=0:
					print os.getcwd()
                                        if self.script12 == "1st":
				          my_name="python Extract_html.py "+self.file1+" "+text_file+" "+self.final
				          os.system(my_name)
					  os.chdir("WalkMan-Chanakya-FontConverter")
					  os.system("sh compile.sh")
					  sdf123="sh fontconversion.sh "+text_file
					  os.system(sdf123)
					  fsdsadfasdf=text_file+".utf8"
					  #print fsdsadfasdf
					  f=open(fsdsadfasdf,'r')
					  old = f.read();
					  f.close();
					  new = old.split('\n');
					  new = " ".join(new);
					  new = re.sub('\|',"|\n",new);
					  new = re.sub('\?',"?\n",new);
					  new = re.sub('!',"!\n",new);
                                          new = new.replace("\n|\n","\n");
                                          new = new.replace("\n|\n","\n");
                                          new = new.replace("\n|\n","\n");
                                          new = new.replace("\n|\n","\n");
                                          new = new.replace("\n|\n","\n");
                                          m=new.split("\n",1)
                                          if m[0]=="|":
                                            new = m[1]
					  po123312="rm -r "+text_file+".*"
					  os.system(po123312)
					  os.remove(text_file)
					  os.chdir("..")
                                        elif self.script12 == "2nd":
				          my_name="python Extract_html.py "+self.file1+" "+text_file+" "+self.final
				          os.system(my_name)
                                          f = open(text_file,'r');
                                          old = f.read();
                                          f.close();
					  new = old.split('\n');
				          new = " ".join(new);
                                          os.remove(text_file)
                                        elif self.script12 == "3rd":
				          my_name="python Extract_html.py "+self.file1+" "+text_file+" "+self.final
				          os.system(my_name)
                                          f = open(text_file,'r')
                                          new = f.read()
                                          f.close()
                                          os.remove(text_file)
		else:
				if(re.search('.+\.ps',self.file1)):
						ret = subprocess.call(["ps2pdf", self.file1])
						if ret == 0:
							self.file1 = self.file1[0:-1] + "df"
							print "success"
						else:
							print "failure"
				if(re.search('.+\.pdf',self.file1)):
						subprocess.call(["pdftohtml","-nomerge","-i","-c",self.file1]);
						text_file = self.file1.replace('.pdf','.txt');
						orig_stdout = sys.stdout;
						fp = open(text_file,'a+')
						sys.stdout = fp
						page_no = 1;
						while(1):
								var = str(page_no);
								var = '-' + var + '.html';
								html_file = self.file1.replace('.pdf',var);
				                                #my_name="python Extract_html.py "+html_file +" "+text_file+" "+self.final
								#os.system(my_name)
                                                                if(os.path.isfile(html_file)):
									try:
										with open(html_file) as f:
											f.close();
											soup = BeautifulSoup(open(html_file));
											comments = soup.find(text=re.compile("<!--"));
											extract_text = soup.get_text();
											extract_text = extract_text.replace(comments,'');
											print extract_text;
										os.remove(html_file);
									except IOError:
										break;
									page_no = page_no+1;
								else:
									break;
                      				sys.stdout = orig_stdout
						fp.close();
						html_file = self.file1.replace('.pdf','.html');
						os.remove(html_file);
						html_file = self.file1.replace('.pdf','_ind.html');
						os.remove(html_file);
						f = open(text_file,'r');
						old = f.read();
						f.close();
						old = re.sub('htmlPage \d\n','\n',old);
				                if cmp(self.final,"English")==0:
						  new = old.split('\n');
                                                  new = " ".join(new);
                                                  new = old.split('\n');
                                                  new = " ".join(new);
                                                  new=re.sub('(?<!www)(?<![\s\n][0-9])\.(?!com)',".\n",new)
                                                  new = re.sub('\?',"?\n",new);
                                                  new = re.sub('!',"!\n",new);
                                                  new=new.replace("\n.\n","\n");
                                                  new=new.replace("\n.\n","\n");
                                                  new=new.replace("\n.\n","\n");
                                                  new=new.replace("\n.\n","\n");
                                                  new=new.replace("\n.\n","\n");
                                                  l=new.split("\n",1)
                                                  if l[0]==".":
                                                    new = l[1]
                                                  os.remove(text_file);
                                                elif cmp(self.final,"English")!=0:
					          print os.getcwd()
                                                  if self.script12 == "1st":
                                                    os.chdir("WalkMan-Chanakya-FontConverter")
                                                    os.system("sh compile.sh")
                                                    sdf123="sh fontconversion.sh "+text_file
                                                    os.system(sdf123)
                                                    fsdsadfasdf=text_file+".utf8"
                                                    f=open(fsdsadfasdf,'r')
                                                    old = f.read();
                                                    f.close();
                                                    new = old.split('\n');
                                                    new = " ".join(new);
                                                    new = re.sub('\|',"|\n",new);
                                                    new = re.sub('\?',"?\n",new);
                                                    new = re.sub('!',"!\n",new);
                                                    new = new.replace("\n|\n","\n");
                                                    new = new.replace("\n|\n","\n");
                                                    new = new.replace("\n|\n","\n");
                                                    new = new.replace("\n|\n","\n");
                                                    new = new.replace("\n|\n","\n");
                                                    m=new.split("\n",1)
                                                    if m[0]=="|":
                                                      new = m[1]
					            po123312="rm -r "+text_file+".*"
					            os.system(po123312)
					            os.remove(text_file)
					            os.chdir("..")
                                                  elif self.script12 == "2nd":
                                                    f = open(text_file,'r');
                                                    old = f.read();
                                                    f.close();
                                                    new = old.split('\n');
                                                    new = " ".join(new);
                                                    new = new.replace("\n।\n","\n");
                                                    new = new.replace("\n।\n","\n");
                                                    new = new.replace("\n।\n","\n");
                                                    new = new.replace("\n।\n","\n");
                                                    new = new.replace("\n।\n","\n");
                                                    m=new.split("\n",1)
                                                    if m[0]=="|":
                                                      new = m[1]
                                                    os.remove(text_file)
                                                  elif self.script12 == "3rd":
                                                    f = open(text_file,'r')
                                                    new = f.read()
                                                    f.close()
                                                    os.remove(text_file)
		dialog = gtk.FileChooserDialog("Save",None,gtk.FILE_CHOOSER_ACTION_SAVE,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
				#gtk.file_chooser.set_do_overwrite_confirmation (GTK_FILE_CHOOSER (dialog), TRUE);
				#dialog.set_current_name(text_file)
		response = dialog.run()
		dialog.set_filename(text_file)
		if response == gtk.RESPONSE_OK:
				filename=dialog.get_filename()
				print filename
				print 'selected'
        			f = open(filename,'w');
				f.write(new);
				f.close();
				if cmp(self.final,"English")!=0 :
                                  if self.script12 == "2nd":
					if self.ou==1 :
						po=self.file2.split("/")
						ko=po[-1]
						pop=ko.split('.')
						po="/".join(po[:-1])
						go1=filename.split("/")
						g1=go1[-1]
						go="/".join(go1[:-1])
						if cmp(pop[-1],"js")==0 :
							mo="node "+po+"/./"+ko+" "+filename+" > "+ go+"/asdf"
						else:
							mo=po+"/./"+ko+" "+filename+" > "+ go+"/asdf"
						self.ou=0
						print mo
						os.system(mo)
						g2="mv "+go+"/asdf "+filename
						print g2
						os.system(g2)
						if cmp(pop[-1],"js")==0 :
							g2="mv temp "+filename
							os.system(g2)
							os.system("rm -rf temp")
							f=open(filename,"r")
							a=f.read()
							f.close()
							a = re.sub("\? ","?\n\n",a);
							a = a.replace("।","।"+"\n\n");
							#a = re.sub(u"। ",u"।\n\n",a);
							a = re.sub('! ',"!\n\n",a);
							f = open(filename,'w');
							#print a
							f.write(a);
							f.close();
					else :
						print filename
						call(["node","sample_character_map.js",filename]);
						f= open("temp",'r+')
						a = f.read()
						f.close()
						a = re.sub("\? ","?\n\n",a);
						a = a.replace("।","।"+"\n");
						a = re.sub('! ',"!\n",a);
                                                a = a.replace("\n।\n","\n");
                                                a = a.replace("\n।\n","\n");
                                                a = a.replace("\n।\n","\n");
                                                a = a.replace("\n।\n","\n");
                                                a = a.replace("\n\n\n","");
                                                m=a.split("\n",1)
                                                if m[0]=="।":
                                                    a = m[1]
						f = open(filename,'w');
						f.write(a);
						f.close();
						os.system("rm -rf temp")
				#orig_stdout = sys.stdout;
				#sys.stdout = f;
		elif response == gtk.RESPONSE_CANCEL:
				print 'Closed, no files selected'
	#	sys.stdout = orig_stdout
		dialog.destroy()
		self.page_1()
	def asdf1(self,widget,asdf21):
		self.window1.destroy()
		self.window.show()
	def asdf(self,widget):
		self.window1.destroy
		self.window.show()
	def func(self):
		abc=self.file1.split('.')
		if self.final!="English" and (cmp(abc[-1],"pdf")==0 or cmp(abc[-1],"ps")==0) :
			self.script12="2nd"
			self.func1()
		elif self.final!="English" :
			self.helloflag=1
			self.helloflag1=1
			self.main_vbox1 = gtk.VBox(False, 0)
			self.window.add(self.main_vbox1)
			frame_vert = gtk.Frame()
			self.main_vbox1.pack_start(frame_vert, True, True, 10)
			hbox = gtk.HBox(False, 0)
			hbox.set_border_width(10)
			frame_vert.add(hbox)
			hbox.pack_start(self.create_bbox1(True, "Selection",
				5, gtk.BUTTONBOX_START),
				True, True, 0)
			frame_horz = gtk.Frame()
			self.main_vbox1.pack_start(frame_horz, True, True, 10)
			vbox = gtk.HBox(False, 0)
			vbox.set_border_width(10)
			frame_horz.add(vbox)
			vbox.pack_start(self.create_bbox1(False, "        ",5, gtk.BUTTONBOX_END),True, True, 0)
			self.window.show_all()
		else :
			self.hello()
	def func1(self) :
		self.main_vbox1 = gtk.VBox(False, 0)
		self.window.add(self.main_vbox1)
		frame_vert = gtk.Frame()
		self.main_vbox1.pack_start(frame_vert, True, True, 10)
		hbox = gtk.HBox(False, 0)
		hbox.set_border_width(10)
		frame_vert.add(hbox)
		frame_horz = gtk.Frame()
		hbox.pack_start(self.create_bbox123(True, "Selection",
				5, gtk.BUTTONBOX_START),
				True, True, 0)
		frame_horz = gtk.Frame()
		self.main_vbox1.pack_start(frame_horz, True, True, 10)
		vbox = gtk.HBox(False, 0)
		vbox.set_border_width(10)
		frame_horz.add(vbox)
		vbox.pack_start(self.create_bbox123(False, "        ",5, gtk.BUTTONBOX_END),True, True, 0)
		self.window.show_all()
	def create_bbox123(self, horizontal, title, spacing, layout):
		frame = gtk.Frame(title)
		if horizontal:
			bbox = gtk.VButtonBox()
			bbox.set_border_width(10)
			frame.add(bbox)
			hbox = gtk.HBox(False, 0)
			hbox.set_border_width(1)
			self.entry1234=gtk.Entry(max=0)
			self.entry1234.set_editable(False)
			self.entry1234.show()
			hbox.pack_start(self.entry1234,True,True,0)
			label=gtk.Label("Enter Mapping Script ")
			bbox.add(label)
			button = gtk.Button()
			box3 = xpm_label_box(self.window, "info.xpm", "Browse")
			map = button.get_colormap()
	 		color = map.alloc_color("light blue")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)

			button.connect_object("clicked", self.file_back123,None,"English")
			button.set_tooltip_text("Press this button to browse the Mapping script")
			button.add(box3)
			box3.show()

			hbox.add(button)
			bbox.add(hbox)


			self.bbox.set_layout(layout)
			self.bbox.set_spacing(spacing)

		else:
			bbox = gtk.HButtonBox()
			bbox.set_border_width(10)
			frame.add(bbox)
			bbox.set_layout(layout)
			bbox.set_spacing(spacing)
			vbox = gtk.HButtonBox()
			vbox.set_layout(layout)
			vbox.set_border_width(1)
			button = gtk.Button(stock="Submit")
			map = button.get_colormap()
	 		color = map.alloc_color("light green")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)
			button.connect_object("clicked", self.submit_application123, self.window,None)
			button.set_tooltip_text("Submit")
			vbox.add(button)
			button = gtk.Button(stock="Back")
			map = button.get_colormap()
	 		color = map.alloc_color("gray")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)
			button.connect_object("clicked", self.Back_application123, self.window,None)
			button.set_tooltip_text("Back To Document Conversion Tool")
			vbox.add(button)
			bbox.add(vbox)
		return frame
	def callback1(self, widget, data=None):
		if(("ON")[widget.get_active()]):
			self.script=data;
	def submit_application123(self, widget, event, data=None):
		print self.script12
		print self.file21
		self.window.remove(self.main_vbox1)
		self.hello()
	def submit_application(self, widget, event, data=None):
		print self.file1
		print self.final
		print self.file2
		if self.file1 !=-1 :
			abc=self.file1.split('.')
			print abc
			flag12=0
			if self.file2!=-1 :
				 g=subprocess.check_output(["ls","-lh",self.file2])
				 g=g.split(' ')[0].split('-')
				 print g
				 if cmp(g[1],"rwxr")==0 and cmp(g[2],"x")==0 and cmp(g[4],"x")==0:
					 flag12=1
			if cmp(abc[-1],"pdf")==0 or cmp(abc[-1],"ps")==0 or cmp(abc[-1],"txt")==0 or cmp(abc[-1],"html")==0 or cmp(abc[-1],"htm")==0:
				if flag12 ==0 and self.file2!=-1 :
					self.window.hide()
					self.window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
					color = gtk.gdk.color_parse('white smoke')
					self.window1.modify_bg(gtk.STATE_NORMAL, color)

					self.window1.set_title("Error")
					self.window1.connect("destroy",self.asdf)
					label = gtk.Label("\n\n\nThe character mapping script should be executable file")
					label.show()
					self.window1.set_size_request(400, 200)
					bbox = gtk.VButtonBox()
					bbox.set_border_width(10)
					self.window1.add(bbox)
					bbox.add(label)

					button = gtk.Button(stock="Okay")
					button.connect_object("clicked",self.asdf1,self.window1,None)
					button.set_tooltip_text("Close this window")
					button.show()
					bbox.pack_start(button)
					self.window1.show_all()
				else:
					if self.file2==-1 :
						self.window.remove(self.main_vbox)
						self.func()
					#	self.hello()
					else :
						self.window.remove(self.main_vbox)
						self.ou=1
						self.func()
					#	self.hello()
			else :
				if flag12==0 and self.file2!=-1 :
					self.window.hide()
					self.window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
					color = gtk.gdk.color_parse('white smoke')
					self.window1.modify_bg(gtk.STATE_NORMAL, color)

					self.window1.set_title("Error")
					self.window1.connect("destroy",self.asdf)
					label = gtk.Label("\n\n\nThe character mapping script should be executable file\n and Given input file should be in specified formats ")
					label.show()
					self.window1.set_size_request(400, 250)

					bbox = gtk.VButtonBox()
					bbox.set_border_width(10)
					self.window1.add(bbox)
					bbox.add(label)

					button = gtk.Button(stock="Okay")
					button.connect_object("clicked",self.asdf1,self.window1,None)
					button.set_tooltip_text("Close this window")
					button.show()
					bbox.pack_start(button)
					self.window1.show_all()
				else:
					self.window.hide()
					self.window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
					color = gtk.gdk.color_parse('white smoke')
					self.window1.modify_bg(gtk.STATE_NORMAL, color)

					self.window1.set_title("Error")
					self.window1.connect("destroy",self.asdf)
					label = gtk.Label("\n\n\nGiven input file is not of specified formats")
					label.show()
					self.window1.set_size_request(400, 200)

					bbox = gtk.VButtonBox()
					bbox.set_border_width(10)
					self.window1.add(bbox)
					bbox.add(label)

					button = gtk.Button(stock="Okay")
					button.connect_object("clicked",self.asdf1,self.window1,None)
					button.set_tooltip_text("Close this window")
					button.show()
					bbox.pack_start(button)
					bbox.show()
					self.window1.show_all()
		else:
			self.window.hide()
			self.window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
			color = gtk.gdk.color_parse('white smoke')
			self.window1.modify_bg(gtk.STATE_NORMAL, color)

			self.window1.set_title("Error")
			self.window1.connect("destroy",self.asdf)
			label = gtk.Label("\n\n\nFile not given")
			label.show()
			self.window1.set_size_request(400, 200)

			bbox = gtk.VButtonBox()
			bbox.set_border_width(10)
			self.window1.add(bbox)
			bbox.add(label)

			button = gtk.Button(stock="Okay")
			button.connect_object("clicked",self.asdf1,self.window1,None)
			button.set_tooltip_text("Close this window")
			button.show()
			bbox.pack_start(button)
			bbox.show()
			self.window1.show_all()
	def Back_application(self, widget, event, data=None):
		self.window.remove(self.main_vbox)
		self.label123=-1
		self.script="1st"
		self.script12="3rd"
		self.entry1234=-1
		self.world=-1
		self.file1=-1
		self.file21=-1
		self.final="English"
		self.file2=-1
		self.file5=-1
		self.file6=-1
		self.file21=-1
		self.file7=-1
		self.ou=0
		self.entry1=-1
		self.entry=-1
		self.entry2=-1
		self.entry5=-1
		self.entry7=-1
		self.helloflag=0
		self.helloflag1=0
		self.entry7=-1
		self.page_1()
	def Back_application123(self, widget, event, data=None):
		self.window.remove(self.main_vbox1)
		self.label123=-1
		self.script12="3rd"
		self.world=-1
		self.file21=-1
		self.entry1234=-1
		self.file2=-1
		self.file5=-1
		self.file6=-1
		self.file7=-1
		self.ou=0
		self.entry1=-1
		self.entry=-1
		self.entry2=-1
		self.entry5=-1
		self.entry7=-1
		self.helloflag=0
		self.helloflag1=0
		self.file21=-1
		self.entry7=-1
		self.func()
	def Back_application12(self, widget, event, data=None):
		self.window.remove(self.main_vbox1)
		self.helloflag1=0
		self.helloflag=0
		self.label123=-1
		self.script="1st"
		self.entry1234=-1
		self.script12="3rd"
		self.world=-1
		self.file1=-1
		self.final="English"
		self.file2=-1
		self.file21=-1
		self.file5=-1
		self.file6=-1
		self.file7=-1
		self.ou=0
		self.entry1=-1
		self.entry=-1
		self.entry2=-1
		self.entry5=-1
		self.entry7=-1
		self.helloflag=0
		self.helloflag1=0
		self.entry7=-1
		self.Document()
	def create_bbox3(self, horizontal, title, spacing, layout):
		frame = gtk.Frame(title)
		if horizontal:
			bbox = gtk.VButtonBox()
			bbox.set_border_width(10)
			frame.add(bbox)
			hbox = gtk.HBox(False, 0)
			hbox.set_border_width(1)
			self.entry5=gtk.Entry(max=0)
			self.entry5.set_editable(False)
			self.entry5.show()
			hbox.pack_start(self.entry5,True,True,0)
			label=gtk.Label("Enter English File")
			bbox.add(label)


			button = gtk.Button()
			box3 = xpm_label_box(self.window, "info.xpm", "Browse")
			map = button.get_colormap()
	 		color = map.alloc_color("light blue")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)

			button.connect_object("clicked", self.file_back3,None,"English")
			button.set_tooltip_text("Press this button to browse the English file")
			button.add(box3)
			box3.show()
			hbox.add(button)
			bbox.add(hbox)


			hbox = gtk.HBox(False, 0)
			hbox.set_border_width(1)
			self.entry6=gtk.Entry(max=0)
			self.entry6.set_editable(False)
			self.entry6.show()
			hbox.pack_start(self.entry6,True,True,0)
			label=gtk.Label("Enter Hindi File")
			bbox.add(label)


			button = gtk.Button()
			box3 = xpm_label_box(self.window, "info.xpm", "Browse")
			map = button.get_colormap()
	 		color = map.alloc_color("light blue")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)

			button.connect_object("clicked", self.file_back3,None,"Hindi")
			button.set_tooltip_text("Press this button to browse the Hindi file")
			button.add(box3)
			box3.show()
			hbox.add(button)
			bbox.add(hbox)



			hbox = gtk.HBox(False, 0)
			hbox.set_border_width(1)
			self.entry7=gtk.Entry(max=0)
			self.entry7.set_editable(False)
			self.entry7.show()
			hbox.pack_start(self.entry7,True,True,0)
			label=gtk.Label("Enter Dictionary")
			bbox.add(label)


			button = gtk.Button()
			box3 = xpm_label_box(self.window, "info.xpm", "Browse")
			map = button.get_colormap()
	 		color = map.alloc_color("light blue")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)

			button.connect_object("clicked", self.file_back3,None,"dict")
			button.set_tooltip_text("Press this button to browse the Dictionary")
			button.add(box3)
			box3.show()
			hbox.add(button)
			bbox.add(hbox)
			label=gtk.Label("If input for dictionary is not given then default dictionary will be used")
			bbox.add(label)




			bbox.set_layout(layout)
			bbox.set_spacing(spacing)
		else :
			self.bbox123 = gtk.HButtonBox()
			self.bbox123.set_border_width(10)
			frame.add(self.bbox123)
			self.bbox123.set_layout(layout)
			self.bbox123.set_spacing(spacing)
			vbox = gtk.HButtonBox()
			vbox.set_layout(layout)
			vbox.set_border_width(1)
			button = gtk.Button(stock="Submit")
			map = button.get_colormap()
	 		color = map.alloc_color("light green")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)
			button.connect_object("clicked", self.submit_application3, self.window,None)
			button.set_tooltip_text("Submit")
			vbox.add(button)
			button = gtk.Button(stock="Back")
			map = button.get_colormap()
	 		color = map.alloc_color("gray")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)
			button.connect_object("clicked", self.Back_application, self.window,None)
			button.set_tooltip_text("Close this window")
			vbox.add(button)
			self.bbox123.add(vbox)
		return frame
	def create_bbox(self, horizontal, title, spacing, layout):
		frame = gtk.Frame(title)
		if horizontal:

			self.obs_box = gtk.VButtonBox()
			#self.main.pack_start(self.obs_box, False, True, 0)
			frame.add(self.obs_box)
			label=gtk.Label("\n")
			self.obs_box.add(label)
			self.combobox_1 = gtk.ComboBox()
			self.liststore = gtk.ListStore(str)
			self.cell = gtk.CellRendererText()
			self.combobox_1.pack_start(self.cell)
			self.combobox_1.add_attribute(self.cell, 'text', 0)
			self.obs_box.pack_start(self.combobox_1, False, True, 3)
			self.liststore.append(['Arabic'])
			self.liststore.append(['Bengali'])
			self.liststore.append(['English'])
			self.liststore.append(['German'])
			self.liststore.append(['Greek'])
			self.liststore.append(['Gujarathi'])
			self.liststore.append(['Hindi'])
			self.liststore.append(['Latin'])
			self.liststore.append(['Russian'])
			self.liststore.append(['Tamil'])
			self.liststore.append(['Telugu'])
			self.combobox_1.set_model(self.liststore)
			self.combobox_1.connect('changed', self.call_back)
			self.combobox_1.set_active(2)
			self.obs_box.set_layout(layout)
			self.obs_box.set_spacing(spacing)
			label=gtk.Label("\n")
			self.obs_box.add(label)
		else:
			label=gtk.Label("Insert the input file")
			bbox = gtk.VButtonBox()
			bbox.set_border_width(10)
			frame.add(bbox)
			hbox = gtk.HBox(False, 0)
			hbox.set_border_width(1)
			self.entry=gtk.Entry(max=0)
			self.entry.set_editable(False)
			self.entry.show()
			hbox.pack_start(self.entry,True,True,0)
			bbox.add(label)


			button = gtk.Button()
			box3 = xpm_label_box(self.window, "info.xpm", "Browse")
			map = button.get_colormap()
	 		color = map.alloc_color("light blue")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)

			button.connect_object("clicked", self.file_back,None)
			button.set_tooltip_text("Press this button to browse the file")
			button.add(box3)
			box3.show()
			hbox.add(button)
			bbox.add(hbox)
			bbox.set_layout(layout)
			bbox.set_spacing(spacing)
			vbox = gtk.HButtonBox()
			vbox.set_layout(layout)
			vbox.set_border_width(1)

			button = gtk.Button(stock="Back")
			button.connect_object("clicked", self.Back_application, self.window,None)
			button.set_tooltip_text("Redirect to First page")
			vbox.add(button)

			button = gtk.Button(stock="Submit")
			map = button.get_colormap()
	 		color = map.alloc_color("light green")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)
			button.connect_object("clicked", self.submit_application, self.window,None)
			button.set_tooltip_text("Submit")
			vbox.add(button)
			button = gtk.Button(stock="Close")
			map = button.get_colormap()
	 		color = map.alloc_color("gray")
			style = button.get_style().copy()
	 		style.bg[gtk.STATE_NORMAL] = color
	    		button.set_style(style)
			button.connect_object("clicked", self.close_application, self.window,None)
			button.set_tooltip_text("Close this window")
			vbox.add(button)
			bbox.add(vbox)
		return frame
	def __init__(self):
		self.script="1st"
		self.script12="3rd"
		self.world=-1
		self.file1=-1
		self.entry1234=-1
		self.final="English"
		self.file2=-1
		self.label123=-1
		self.helloflag=0
		self.helloflag1=0
		self.file21=-1
		self.ou=0
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		color = gtk.gdk.color_parse('white smoke')
		self.window.modify_bg(gtk.STATE_NORMAL, color)

		self.window.set_title("Document Conversion Tool")
		self.window.connect("destroy", lambda x: gtk.main_quit())
		self.window.set_size_request(500, 500)
		#self.Document()
		self.page_1()
		self.window.show_all()
	def main(self):
		gtk.main()
if __name__ == "__main__":
	a=ButtonBoxExample()
	a.main()
