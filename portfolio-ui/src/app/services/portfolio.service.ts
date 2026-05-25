import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ProfileDataResponse, AiAgentQueryResponse } from '../models/portfolio.model';

@Injectable({
  providedIn: 'root'
})
export class PortfolioService {
  private baseUrl = 'http://127.0.0.1:8000/api/v1/portfolio';

  constructor(private http: HttpClient) {}

  getProfileData(): Observable<ProfileDataResponse> {
    return this.http.get<ProfileDataResponse>(`${this.baseUrl}/profile`);
  }

  queryAiAgent(query: string): Observable<AiAgentQueryResponse> {
    return this.http.post<AiAgentQueryResponse>(`${this.baseUrl}/agent/query`, { query });
  }
}