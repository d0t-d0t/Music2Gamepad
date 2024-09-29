from pythonosc import udp_client, dispatcher, osc_server
import threading

class AbletonLink:
    def __init__(self, metronome, ip='127.0.0.1', send_port=11000, receive_port=11001):
        self.metronome = metronome
        self.beatmaster = metronome.beatmaster
        self.beatmaster.add_observer(self,observer_type=['tonality','bpm','play'])
        self.client = udp_client.SimpleUDPClient(ip, send_port)

        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/live/test", self.test_handler)

        self.server = osc_server.ThreadingOSCUDPServer((ip, receive_port), self.dispatcher)
        print("Serving on {}".format(self.server.server_address))

        # Start the server in a new thread
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

        # Send a test message to Ableton
        self.client.send_message('/live/test', [])

        

        

    def test_handler(self, addr, args):
        print('Received response from Ableton Link:', args)

    def on_bpm_change(self, bpm):
        self.client.send_message('/live/song/set/tempo', bpm)
    
    def on_tonal_change(self, tonality):
        self.client.send_message('/live/song/set/key', tonality)

    def on_signature_numerator_change(self, signature_numeral):
        self.client.send_message('/live/song/set/signature_numerator', signature_numeral)
    
    def on_signature_denominator_change(self, signature_denominator):
        self.client.send_message('/live/song/set/signature_denominator', signature_denominator)
    

    def on_play(self):
        self.client.send_message('/live/song/continue_playing', [])

    def on_stop(self):
        self.client.send_message('/live/song/stop_playing', [])
    
    def on_metronome_switch(self,value = 1):
        self.client.send_message('/live/song/set/metronome',value)
