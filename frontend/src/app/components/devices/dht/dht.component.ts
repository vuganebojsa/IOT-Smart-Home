import { Component } from '@angular/core';

@Component({
  selector: 'app-dht',
  templateUrl: './dht.component.html',
  styleUrls: ['./dht.component.css']
})
export class DhtComponent {
  measurementName: 'measurement_humidity';
  measurementSecondName: 'measurement_temperature';
  deviceName: 'DHT';
}
