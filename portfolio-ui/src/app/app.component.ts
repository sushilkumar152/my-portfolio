import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PortfolioService } from './services/portfolio.service';
import { ProfileDataResponse, AiAgentQueryResponse } from './models/portfolio.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  profileData!: ProfileDataResponse;
  isLoadingProfile = true;
  
  // AI Agent States
  userQuery = '';
  agentResponse: AiAgentQueryResponse | null = null;
  isLoadingAgent = false;

  constructor(private portfolioService: PortfolioService) {}

  ngOnInit(): void {
    this.portfolioService.getProfileData().subscribe({
      next: (data) => {
        this.profileData = data;
        this.isLoadingProfile = false;
      },
      error: (err) => {
        console.error('Failed to fetch profile data', err);
        this.isLoadingProfile = false;
      }
    });
  }

  submitAgentQuery(): void {
    if (!this.userQuery.trim() || this.isLoadingAgent) return;

    this.isLoadingAgent = true;
    this.portfolioService.queryAiAgent(this.userQuery).subscribe({
      next: (res) => {
        this.agentResponse = res;
        this.isLoadingAgent = false;
      },
      error: (err) => {
        console.error('Agent lookup failure', err);
        this.isLoadingAgent = false;
      }
    });
  }
}