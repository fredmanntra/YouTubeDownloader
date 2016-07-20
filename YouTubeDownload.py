def main():
  from pytube import YouTube

##Get web address from user
  error = True
  while error == True:
    http = raw_input('Paste YouTube address here, then press enter --> ')
    if http == 'q':
      return(0)
    try:
      yt = YouTube(http)
      error = False
    except:
      print('Invalid web address, try again or enter q to quit!')

##Get list of videos and display to user (including video index)
  vids = yt.get_videos()
  print
  for vid in vids:
    print(str(vids.index(vid)) + ' ' + str(vid))

##Prompt user for choice of video to download (user entry must be valid index #)
  numberOfVids = len(vids)
  error = True
  while error == True:
    print
    vidIndexStr = raw_input('Which video number? (0 - ' + str(numberOfVids - 1) + ') -->')
    if vidIndexStr == 'q':
      return(0)    
    try:
      print
      vidIndex = int(vidIndexStr)
      vids[vidIndex].download('C:/Python27/')
      error = False
    except:
      print('Error..Either Invalid video number or file already exists, try again or enter q to quit!')


if __name__ == '__main__': 
    main()
