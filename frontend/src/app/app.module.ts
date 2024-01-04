import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomeComponent } from './components/home/home.component';
import { AlarmClockComponent } from './components/alarm-clock/alarm-clock.component';
import { HouseAlarmComponent } from './components/house-alarm/house-alarm.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {NgxMaterialTimepickerModule} from 'ngx-material-timepicker';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { DeviceInfoComponent } from './components/device-info/device-info.component';
import { BrgbComponent } from './components/devices/brgb/brgb.component';
import { DhtComponent } from './components/devices/dht/dht.component';
import { DisplayDeviceComponent } from './components/display-device/display-device.component';
import { DmsComponent } from './components/dms/dms.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RgbComponent } from './components/rgb/rgb.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    AlarmClockComponent,
    HouseAlarmComponent,
    DeviceInfoComponent,
    BrgbComponent,
    DhtComponent,
    DisplayDeviceComponent,
    DmsComponent,
    RgbComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    NgxMaterialTimepickerModule,
    MatSnackBarModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
