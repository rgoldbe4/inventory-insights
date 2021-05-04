import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SplashNavComponent } from './splash-nav.component';

describe('SplashNavComponent', () => {
  let component: SplashNavComponent;
  let fixture: ComponentFixture<SplashNavComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SplashNavComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SplashNavComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
