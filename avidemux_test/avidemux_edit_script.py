
adm = Avidemux()
adm.loadVideo(r"J:\_Write_Mi\roku_save_241006\_ss\rem ss\_ss 84336008ss013 2023年01月21日19時32分51秒(84336008).ts")
adm.clearSegments()
adm.addSegment(0, 10000, 60000)
adm.setContainer("MP4")
adm.save(r"J:\avidemux_files\avidemux_output\_ss 84336008ss013 2023年01月21日19時32分51秒(84336008).ts")
    